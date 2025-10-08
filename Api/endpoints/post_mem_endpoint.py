import requests


from Api.endpoints.general_endpoint import GeneralMethods


class PostMem(GeneralMethods):
    def create_mem(self, body, token):
        self.response = requests.post(url=f'{self.url}/meme', json=body, headers=self._headers(token))
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response, self.json
