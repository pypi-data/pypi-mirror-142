import requests
import json
import subprocess
import traceback
import time
import logging


class DataSphereApiClient:
    def __init__(self, token_provider, folder_id=None, rest_endpoint=None, grpc_endpoint=None):
        self._token_provider = token_provider
        self._default_folder = folder_id
        self._logger = logging.getLogger()
        self._rest_endpoint = 'https://datasphere.api.cloud.yandex.net/datasphere/v1' if rest_endpoint is None else rest_endpoint
        self._grpc_endpoint = 'yds.api.yandexcloud.net:9090' if grpc_endpoint is None else grpc_endpoint
        self._operation_api_endpoint = 'https://operation.api.cloud.yandex.net'

    def create_project(self, project_name, service_account_id, folder_id=None):
        body = {
            "folderId": self.__resolve_folder(folder_id),
            "name": project_name,
            "settings": {
                "serviceAccountId": service_account_id,
                "commitMode": "STANDARD",
            }
        }

        return self.__call_with_retry(
            lambda: requests.post(url=f"{self._rest_endpoint}/projects", json=body, headers=self.__create_auth_header())
        )

    def create_project_from_checkpoint(self, project_name, service_account_id, checkpoint_id, subnet_id=None, folder_id=None):
        body = {
            "folder_id": self.__resolve_folder(folder_id),
            "name": project_name,
            "settings": {
                "service_account_id": service_account_id
            },
            "parent_checkpoint": checkpoint_id
        }

        if subnet_id is not None:
            body["settings"]["subnet_id"] = subnet_id

        return self.__execute_request(self._grpc_endpoint,
                                      "yandex.cloud.priv.ai.platform.v1.ProjectService/",
                                      "Create",
                                      json.dumps(body),
                                      self._token_provider())

    def get_project_id(self, project_name, folder_id=None):
        page_token = None
        body = {
            "folderId": self.__resolve_folder(folder_id),
            "pageSize": 1000
        }

        while True:
            if page_token is not None:
                body["pageToken"] = page_token

            code, data = self.__call_with_retry(
                lambda: requests.get(url=f"{self._rest_endpoint}/projects", json=body,
                                     headers=self.__create_auth_header())
            )

            if code == 500:
                return None

            page_token = data.get('nextPageToken')

            for proj in data['projects']:
                if proj['name'] == project_name:
                    return proj['id']

    def get_all_projects(self, folder_id=None):
        page_token = None
        body = {
            "folderId": self.__resolve_folder(folder_id),
            "pageSize": 1000
        }

        result = []
        while True:
            if page_token is not None:
                body["pageToken"] = page_token

            code, data = self.__call_with_retry(
                lambda: requests.get(url=f"{self._rest_endpoint}/projects", json=body,
                                     headers=self.__create_auth_header())
            )

            if code == 500:
                return []

            page_token = data.get('nextPageToken')

            for proj in data['projects']:
                result.append((proj['id'], proj['name']))

            if page_token is None:
                return result

    def get_notebook_metadata(self, project_id, notebook_path):
        code, data = self.__call_with_retry(
            lambda: requests.get(
                url=f"{self._rest_endpoint}/projects/{project_id}:notebookMetadata?notebookPath={notebook_path}",
                headers=self.__create_auth_header(),
            )
        )

        if code == 500:
            return None

        return data

    def execute(self, project_id, input_vars, output_vars_names, sync=True, notebook_id=None, cell_id=None):
        body = {
            "inputVariables": input_vars,
            "outputVariableNames": output_vars_names,
        }

        if notebook_id is not None:
            body['notebookId'] = notebook_id
        elif cell_id is not None:
            body['cellId'] = cell_id

        code, data = self.__call_with_retry(
            lambda: requests.post(
                url=f"{self._rest_endpoint}/projects/{project_id}:execute",
                json=body,
                headers=self.__create_auth_header(),
            )
        )

        if sync and code != 500:
            operation_id = data['id']
            return self.__wait_operation(operation_id)

        return data

    def __create_auth_header(self):
        return {'Authorization': f'Bearer {self._token_provider()}'}

    def __call_with_retry(self, callable, tries=10):
        while tries > 0:
            response = callable()

            if 200 <= response.status_code < 300:
                return response.status_code, response.json()

            tries -= 1

        return 500, {}

    def __get_operation_status(self, operation_id):
        r = requests.get(
            url=f"{self._operation_api_endpoint}/operations/{operation_id}",
            headers=self.__create_auth_header(),
        )

        if 200 <= r.status_code < 300:
            return r.json()

        raise ValueError(f"Create project failed, code: {r.status_code}")

    def __wait_operation(self, operation_id):
        status = self.__get_operation_status(operation_id)
        while not status['done']:
            status = self.__get_operation_status(operation_id)
            time.sleep(1)

        maybe_error = status.get('error')
        if maybe_error is not None:
            raise ValueError(maybe_error["message"] + f" Operation id = {operation_id}")

        return status

    def __execute_request(self, host, endpoint, method, request, token):
        while True:
            try:
                proc = subprocess.run([
                    'grpcurl',
                    '-rpc-header', 'Authorization: Bearer ' + token,
                    '-d', request,
                    host, endpoint + method,
                ], stdout=subprocess.PIPE)

                return proc.returncode, proc.stdout.decode("utf-8")
            except:
                traceback.print_exc()
                time.sleep(1)

    def __resolve_folder(self, folder):
        if folder is None:
            return self._default_folder
        return folder

