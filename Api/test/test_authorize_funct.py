import pytest
import allure


@allure.title('Authorize in system')
@allure.story('authorize for user')
@pytest.mark.positive
@pytest.mark.parametrize('body', [{"name": "Testov"}])
def test_authorize(authorize_endpoints, body):
    authorize_endpoints.user_authorize(body)
    authorize_endpoints.check_status_code_is_200()
    authorize_endpoints.check_token_is_not_null()
    authorize_endpoints.check_user(body)


@allure.title('Authorize in system')
@allure.story('authorize for user')
@pytest.mark.negative
@pytest.mark.parametrize('body', [{},
                                  {"name": None},
                                  {"name": ["Тестов"]},
                                  {"name": 1}])
def test_negative_authorize(authorize_endpoints, body):
    authorize_endpoints.user_authorize(body)
    authorize_endpoints.check_status_code_is_400()
