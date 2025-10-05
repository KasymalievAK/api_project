import requests


from Api.methods.general import GeneralMethods


class GetMethod(GeneralMethods):
    def method_get_mem(self, token, object_id):
        self.response = requests.get(url=f"{self.url}/meme/{object_id}", headers=self._headers(token))
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response, self.json
