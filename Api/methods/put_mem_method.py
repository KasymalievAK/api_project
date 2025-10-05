import requests


from Api.methods.general import GeneralMethods


class PutMem(GeneralMethods):
    def method_for_put_mem(self, object_id, token, body):
        self.response = requests.put(url=f"{self.url}/meme/{object_id}", json=body, headers=self._headers(token))
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.json, self.response
