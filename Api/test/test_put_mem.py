import pytest
import allure


@allure.title('Put mem')
@allure.feature('mem CRUD')
@allure.story('Update info about mem')
@pytest.mark.positive
def test_put_mem(fix_test_token, fix_test_mem, fix_put_mem):
    object_id = fix_test_mem.object_id
    body = {"id": object_id, "text": "лягушка", "url": "https://cs20.pikabu.ru/s/2025/09/28/17/df42xki4.webp",
            "tags": ["Юмор", "Комиксы"], "info": {"раздел": "Лига биологов", "автор": "REDLIS"}}
    fix_put_mem.method_for_put_mem(object_id, fix_test_token.token, body)
    fix_put_mem.check_status_code_is_200()
    fix_put_mem.check_text_in_response(body)
    fix_put_mem.check_url_in_response(body)
    fix_put_mem.check_tags_in_response(body)
    fix_put_mem.check_info_in_response(body)


TEST_CASES = [
    # проверка text
    {"name": "text_wrong_type", "body": {"text": 123, "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                         "tags": ["Юмор"], "info": {"автор": "TvoeNastroenie"}}},
    {"name": "without_text", "body": {"url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                      "tags": ["Юмор"], "info": {"автор": "TvoeNastroenie"}}},

    # проверка url
    {"name": "url_wrong_type", "body": {"text": "Единорог", "url": [],
                                        "tags": ["Юмор"], "info": {"автор": "TvoeNastroenie"}}},
    {"name": "without_url", "body": {"text": "Единорог", "tags": ["Юмор"], "info": {"автор": "TvoeNastroenie"}}},

    # проверка tags
    {"name": "tags_wrong_type", "body": {"text": "Единорог",
                                         "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                         "tags": {},
                                         "info": {"категория": "Животные"}}},
    {"name": "without_tags", "body": {"text": "Единорог",
                                      "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                      "info": {"категория": "Животные"}}},

    # проверка info
    {"name": "info_wrong_type", "body": {"text": "Единорог",
                                         "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                         "tags": ["Юмор"],
                                         "info": 1}},
    {"name": "info_missing", "body": {"text": "Единорог",
                                      "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                      "tags": ["Юмор"]}}
]


@allure.title('Put mem')
@allure.feature('mem CRUD')
@allure.story('Update info about mem')
@pytest.mark.negative
@pytest.mark.parametrize("body", TEST_CASES, ids=[c["name"] for c in TEST_CASES])
def test_put_mem_negative(fix_test_token, fix_test_mem, fix_put_mem, body):
    body["id"] = fix_test_mem.object_id
    fix_put_mem.method_for_put_mem(fix_test_mem.object_id, fix_test_token.token, body)
    fix_put_mem.check_status_code_is_400()


@allure.title('Put mem')
@allure.feature('mem CRUD')
@allure.story('Update info about mem')
@pytest.mark.negative
def test_put_without_token(fix_put_mem, fix_test_mem):
    body = {"id": fix_test_mem.object_id, "text": "лягушка",
            "url": "https://cs20.pikabu.ru/s/2025/09/28/17/df42xki4.webp",
            "tags": ["Юмор", "Комиксы"], "info": {"раздел": "Лига биологов", "автор": "REDLIS"}}
    token = ''
    fix_put_mem.method_for_put_mem(fix_test_mem.object_id, token, body)
    fix_put_mem.check_status_code_is_401()


@allure.title('Put mem')
@allure.feature('mem CRUD')
@allure.story('Update info about mem')
@pytest.mark.negative
def test_put_another_token(fix_test_token, fix_test_mem, fix_put_mem):
    body = {"id": fix_test_mem.object_id, "text": "лягушка",
            "url": "https://cs20.pikabu.ru/s/2025/09/28/17/df42xki4.webp",
            "tags": ["Юмор", "Комиксы"], "info": {"раздел": "Лига биологов", "автор": "REDLIS"}}

    fix_put_mem.method_for_put_mem(fix_test_mem.object_id, fix_test_token.another_token, body)
    fix_put_mem.check_status_code_is_403()
