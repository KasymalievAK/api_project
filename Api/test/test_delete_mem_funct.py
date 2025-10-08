import pytest
import allure


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.positive
def test_delete_mem(test_token_manager, create_test_mem, delete_mem_endpoint, get_mem_endpoint):
    delete_mem_endpoint.method_delete_mem(create_test_mem.object_id, test_token_manager.token)
    print(create_test_mem.object_id)
    delete_mem_endpoint.check_status_code_is_200()


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.negative
def test_delete_mem_negative(create_test_mem, test_token_manager, delete_mem_endpoint):
    delete_mem_endpoint.method_delete_mem(create_test_mem.object_id, test_token_manager.another_token)
    delete_mem_endpoint.check_status_code_is_403()


@allure.title('Delete mem')
@allure.feature('mem CRUD')
@allure.story('Delete info about mem')
@pytest.mark.negative
def test_delete_mem_without_token(create_test_mem, delete_mem_endpoint):
    token = ''
    delete_mem_endpoint.method_delete_mem(create_test_mem.object_id, token)
    delete_mem_endpoint.check_status_code_is_401()
