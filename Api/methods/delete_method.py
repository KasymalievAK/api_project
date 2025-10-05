import requests


from Api.methods.general import GeneralMethods


class DeleteMem(GeneralMethods):
    def method_delete_mem(self, object_id, token):
        self.response = requests.delete(url=f"{self.url}/meme/{object_id}", headers=self._headers(token))
        return self.response
