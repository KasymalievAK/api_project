import requests


from Api.endpoints.general_endpoint import GeneralMethods
from Api.endpoints.get_mem_endpoint import GetMethod


class DeleteMem(GeneralMethods):
    def method_delete_mem(self, object_id, token):
        self.response = requests.delete(url=f"{self.url}/meme/{object_id}", headers=self._headers(token))
        return self.response

    def check_delete_mem(self, token, object_id):
        getter = GetMethod()
        self.response = getter.method_get_mem(token, object_id)
        assert self.response.status_code == 404, (f"Ожидали status_code = 404,"
                                                  f" получили {self.response.status_code}")
