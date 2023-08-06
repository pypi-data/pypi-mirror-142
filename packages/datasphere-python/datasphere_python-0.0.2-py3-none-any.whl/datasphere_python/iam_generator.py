import time
import requests


class RenewableIAMToken:
    def __init__(self, jwt_token_generator):
        self._jwt_token_generator = jwt_token_generator
        self._iam_endpoint = 'https://iam.api.cloud.yandex.net/iam/v1'
        self._cached_token = None
        self._last_updated = None

    def get_iam_token(self):
        if (self._cached_token is None) or ((int(time.time()) - self._last_updated) > 3600.0):
            self._last_updated = int(time.time())
            self._cached_token = self.get_iam_token_from_jwt()

        return self._cached_token

    def get_iam_token_from_jwt(self):
        resp = requests.post(f'{self._iam_endpoint}/tokens',
                             headers={'Content-Type': 'application/json'},
                             json={"jwt": self._jwt_token_generator.generate_jwt()})

        return resp.json()['iamToken']
