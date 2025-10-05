import allure


class GeneralMethods:
    url = 'http://memesapi.course.qa-practice.com'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    def _headers(self, token=None):
        headers = self.headers.copy()
        if token:
            headers['Authorization'] = f'{token}'
        return headers

    @allure.step('Check status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, (f"Ожидали status_code = 200,"
                                                  f" получили {self.response.status_code}")

    @allure.step('Check user')
    def check_user(self, body):
        assert self.json['user'] == body['name'], (f"Ожидали count = {body['name']},"
                                                   f" получили {self.json['user']}")

    @allure.step('Check token')
    def check_token_is_not_null(self):
        assert self.json['token'], "Токен пустой"

    @allure.step('Check status code is 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, (f"Ожидали status_code = 400,"
                                                  f" получили {self.response.status_code}")

    @allure.step("Check token is alive")
    def check_token_status(self, token_status):
        assert token_status, "Токен не активен"

    @allure.step("Check  username created token")
    def check_username_created_token(self, create_name, username):
        assert create_name == username, (f"Ожидали count = {create_name},"
                                         f" получили {username}")

    @allure.step("Check status code is 404")
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, (f"Ожидали status_code = 404,"
                                                  f" получили {self.response.status_code}")

    @allure.step("Check text in response")
    def check_text_in_response(self, body):
        assert self.json['text'] == body['text'], (f"Ожидали text = {body['text']},"
                                                   f" получили {self.json['text']}")

    @allure.step("Check url in response")
    def check_url_in_response(self, body):
        assert self.json['url'] == body['url'], (f"Ожидали url = {body['url']},"
                                                 f" получили {self.json['url']}")

    @allure.step("Check tags in response")
    def check_tags_in_response(self, body):
        json_tags = self.json.get('tags', [])
        body_tags = body.get('tags', [])
        assert json_tags == body_tags, f"Ожидали tags = {body_tags}, получили {json_tags}"

    @allure.step("Check info in response")
    def check_info_in_response(self, body):
        for key, expected_value in body.get('info', {}).items():
            actual_value = self.json.get('info', {}).get(key)
            assert actual_value == expected_value, \
                f"Ожидали {key} = {expected_value}, получили {actual_value}"

    @allure.step("Check without token")
    def check_status_code_is_401(self):
        assert self.response.status_code == 401, (f"Ожидали status_code = 401,"
                                                  f" получили {self.response.status_code}")

    @allure.step("Check another token")
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, (f"Ожидали status_code = 403,"
                                                  f" получили {self.response.status_code}")
