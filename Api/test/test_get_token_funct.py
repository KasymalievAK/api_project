import pytest
import allure


@allure.title('Get token')
@allure.story('authorize for user')
@pytest.mark.positive
def test_get_token(fix_test_token, fix_get_token):
    username, token_status = fix_get_token.method_get_token(fix_test_token.token)
    fix_get_token.check_status_code_is_200()
    fix_get_token.check_token_status(token_status)
    fix_get_token.check_username_created_token(fix_test_token.create_name, username)


@allure.title('Get token')
@allure.story('authorize for user')
@pytest.mark.negative
@pytest.mark.parametrize('token', ["", 12345678, {}, []])
def test_negative_get_token(token, fix_get_token):
    fix_get_token.method_get_token(token)
    fix_get_token.check_status_code_is_404()
