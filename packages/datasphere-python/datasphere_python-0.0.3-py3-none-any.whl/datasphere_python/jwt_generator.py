import time
import jwt


class JWTTokenGenerator:
    def __init__(self, key_id, service_account_id, private_key):
        self.service_account_id = service_account_id
        self.key_id = key_id
        self.private_key = private_key
        self._iam_endpoint = 'https://iam.api.cloud.yandex.net/iam/v1'

    @staticmethod
    def with_file_key(key_id, service_account_id, key_path):
        with open(key_path, 'r') as private:
            private_key = private.read()

        return JWTTokenGenerator(key_id, service_account_id, private_key)

    def generate_jwt(self):
        now = int(time.time())

        payload = {
            'aud': f'{self._iam_endpoint}/tokens',
            'iss': self.service_account_id,
            'iat': now,
            'exp': now + 3600}

        encoded_token = jwt.encode(
            payload,
            self.private_key,
            algorithm='PS256',
            headers={'kid': self.key_id})

        return encoded_token

