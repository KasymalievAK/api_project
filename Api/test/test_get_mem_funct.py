import pytest
import allure


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.positive
def test_get_mem(test_token_manager, create_test_mem, get_mem_endpoint):
    get_mem_endpoint.method_get_mem(test_token_manager.token, create_test_mem.object_id)
    get_mem_endpoint.check_status_code_is_200()
    get_mem_endpoint.check_text_in_response(create_test_mem.json_data)
    get_mem_endpoint.check_url_in_response(create_test_mem.json_data)
    get_mem_endpoint.check_tags_in_response(create_test_mem.json_data)
    get_mem_endpoint.check_info_in_response(create_test_mem.json_data)


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.negative
def test_get_mem_negative(test_token_manager, get_mem_endpoint):
    object_id = ""
    get_mem_endpoint.method_get_mem(test_token_manager.token, object_id)
    get_mem_endpoint.check_status_code_is_404()


@allure.title('Get mem')
@allure.feature('mem CRUD')
@allure.story('info about mem')
@pytest.mark.negative
def test_get_mem_without_token(create_test_mem, get_mem_endpoint):
    token = ''
    get_mem_endpoint.method_get_mem(token, create_test_mem.object_id)
    get_mem_endpoint.check_status_code_is_401()
