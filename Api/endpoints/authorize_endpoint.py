import allure
import requests


from Api.endpoints.general_endpoint import GeneralMethods


class Authorize(GeneralMethods):
    @allure.step('Authorize')
    def user_authorize(self, body):
        self.response = requests.post(url=f"{self.url}/authorize", json=body, headers=self._headers())
        try:
            self.json = self.response.json()
        except ValueError:  # JSONDecodeError
            self.json = None
        return self.json, self.response
