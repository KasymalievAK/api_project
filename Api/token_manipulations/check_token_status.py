import requests
import dotenv
import os


from dotenv import set_key
from dataclasses import dataclass
from Api.endpoints.general_endpoint import GeneralMethods
from Api.endpoints.authorize_endpoint import Authorize


@dataclass
class TokenData:
    token: str
    another_token: str
    create_name: str


class TokenManager(GeneralMethods):
    dotenv.load_dotenv()
    token = os.getenv('actual_token')
    another_token = os.getenv('actual_token_2')
    create_name = os.getenv('create_name')

    def token_status(self, token):
        if not token:
            return False
        else:
            self.response = requests.get(url=f"{self.url}/authorize/{token}")
            return self.response.status_code == 200

    def check_token(self):
        if self.token_status(self.token) and self.token_status(self.another_token):
            return TokenData(token=self.token, another_token=self.another_token, create_name=self.create_name)

        else:
            auth1 = Authorize()
            auth1.user_authorize({"name": "Testislav"})
            token = auth1.json["token"]
            create_name = auth1.json["username"]
            auth2 = Authorize()
            auth2.user_authorize({"name": "Rostislav"})
            another_token = auth2.json["token"]
            set_key(".env", "actual_token", token)
            set_key(".env", "actual_token_2", another_token)
            set_key(".env", "create_name", create_name)
            return TokenData(token=token, another_token=another_token, create_name=create_name)
