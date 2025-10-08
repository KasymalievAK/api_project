import pytest
import allure


@allure.title('Post mem')
@allure.feature('mem CRUD')
@allure.story('Post info about mem')
@pytest.mark.positive
@pytest.mark.parametrize('body', [{"text": "Единорог", "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                   "tags": ['Юмор', 'Единорог', 'Животные'],
                                   "info": {"автор": "TvoeNastroenie", "категория": "Животные",
                                            "раздел": "Смехотворное явление"}},  # Валидные данные
                                  {"text": "Единорог", "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp",
                                   "tags": [],
                                   "info": {"автор": "TvoeNastroenie", "категория": "Животные",
                                            "раздел": "Смехотворное явление"}}])  # пустой массив
def test_post_mem(test_token_manager, create_meme_endpoint, body):
    create_meme_endpoint.create_mem(body, test_token_manager.token)
    create_meme_endpoint.check_status_code_is_200()
    create_meme_endpoint.check_text_in_response(body)
    create_meme_endpoint.check_url_in_response(body)
    create_meme_endpoint.check_tags_in_response(body)
    create_meme_endpoint.check_info_in_response(body)


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


@allure.title('Post mem')
@allure.feature('mem CRUD')
@allure.story('Post info about mem')
@pytest.mark.negative
@pytest.mark.parametrize("body", TEST_CASES, ids=[c["name"] for c in TEST_CASES])
def test_post_mem_negative(test_token_manager, create_meme_endpoint, body):
    create_meme_endpoint.create_mem(body, test_token_manager.token)
    create_meme_endpoint.check_status_code_is_400()


@allure.title('Post mem')
@allure.feature('mem CRUD')
@allure.story('Post info about mem')
@pytest.mark.negative
def test_post_without_token(create_meme_endpoint):
    token = ''
    body = {"text": "Единорог", "url": "https://cs17.pikabu.ru/s/2025/09/27/13/oylvkzxu.webp", "tags": ['Юмор'],
            "info": {"автор": "TvoeNastroenie"}}
    create_meme_endpoint.create_mem(body, token)
    create_meme_endpoint.check_status_code_is_401()
