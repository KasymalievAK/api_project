import pytest
import allure


@allure.title('Get token')
@allure.story('authorize for user')
@pytest.mark.positive
def test_get_token(test_token_manager, get_token_endpoint):
    username, token_status = get_token_endpoint.method_get_token(test_token_manager.token)
    get_token_endpoint.check_status_code_is_200()
    get_token_endpoint.check_token_status(token_status)
    get_token_endpoint.check_username_created_token(test_token_manager.create_name, username)


@allure.title('Get token')
@allure.story('authorize for user')
@pytest.mark.negative
@pytest.mark.parametrize('token', ["", 12345678, {}, []])
def test_negative_get_token(token, get_token_endpoint):
    get_token_endpoint.method_get_token(token)
    get_token_endpoint.check_status_code_is_404()
