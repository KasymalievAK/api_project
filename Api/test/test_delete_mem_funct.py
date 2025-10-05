import pytest
import allure


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.positive
def test_delete_mem(fix_test_token, fix_test_mem, fix_delete_mem):
    fix_delete_mem.method_delete_mem(fix_test_mem.object_id, fix_test_token.token)
    fix_delete_mem.check_status_code_is_200()


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.negative
def test_delete_mem_negative(fix_test_mem, fix_test_token, fix_delete_mem):
    fix_delete_mem.method_delete_mem(fix_test_mem.object_id, fix_test_token.another_token)
    fix_delete_mem.check_status_code_is_403()


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.negative
def test_delete_mem_without_token(fix_test_mem, fix_delete_mem):
    token = ''
    fix_delete_mem.method_delete_mem(fix_test_mem.object_id, token)
    fix_delete_mem.check_status_code_is_401()
