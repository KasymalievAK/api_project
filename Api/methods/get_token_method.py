import requests


from Api.methods.general import GeneralMethods


class GetToken(GeneralMethods):
    def method_get_token(self, token):
        self.response = requests.get(url=f"{self.url}/authorize/{token}", headers=self._headers(token))
        response_text = self.response.text
        if "Username is " in response_text:
            username = response_text.split("Username is ")[1].strip()
        else:
            username = None

        token_status = "Token is alive" in response_text

        self.json = {
            "user": username,
            "token_status": token_status
        }
        return username, token_status
