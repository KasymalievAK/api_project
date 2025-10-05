import pytest
import allure


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.positive
def test_get_mem(fix_test_token, fix_test_mem, fix_get_mem):
    fix_get_mem.method_get_mem(fix_test_token.token, fix_test_mem.object_id)
    fix_get_mem.check_status_code_is_200()
    fix_get_mem.check_text_in_response(fix_test_mem.json_data)
    fix_get_mem.check_url_in_response(fix_test_mem.json_data)
    fix_get_mem.check_tags_in_response(fix_test_mem.json_data)
    fix_get_mem.check_info_in_response(fix_test_mem.json_data)


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.negative
def test_get_mem_negative(fix_test_token, fix_get_mem):
    object_id = ""
    fix_get_mem.method_get_mem(fix_test_token.token, object_id)
    fix_get_mem.check_status_code_is_404()


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.negative
def test_get_mem_without_token(fix_test_mem, fix_get_mem):
    token = ''
    fix_get_mem.method_get_mem(token, fix_test_mem.object_id)
    fix_get_mem.check_status_code_is_401()
