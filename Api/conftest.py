from dataclasses import dataclass

import pytest

from Api.endpoints.authorize_endpoint import Authorize
from Api.endpoints.delete_endpoint import DeleteMem
from Api.endpoints.get_mem_endpoint import GetMethod
from Api.endpoints.get_token_endpoint import GetToken
from Api.endpoints.post_mem_endpoint import PostMem
from Api.endpoints.put_mem_endpoint import PutMem
from Api.token_manipulations.check_token_status import TokenManager


@pytest.fixture()
def authorize_endpoints():
    return Authorize()


@dataclass
class TokenData:
    token: str
    another_token: str
    create_name: str


@pytest.fixture(scope="session")
def test_token_manager():
    manager = TokenManager()
    return manager.check_token()


@pytest.fixture()
def get_token_endpoint():
    return GetToken()


@pytest.fixture()
def create_meme_endpoint():
    return PostMem()


@dataclass
class MemData:
    object_id: int
    json_data: dict


@pytest.fixture()
def create_test_mem(create_meme_endpoint, test_token_manager, delete_mem_endpoint):
    data = {"text": "Мышь", "url": "https://cs18.pikabu.ru/s/2025/09/28/12/vnqrc5ru.webp",
            "tags": ['Ушастый'], "info": {"раздел": "Лига биологов"}}
    response, json_data = create_meme_endpoint.create_mem(data, test_token_manager.token)
    object_id = json_data['id']
    yield MemData(object_id=object_id, json_data=json_data)
    delete_mem_endpoint.method_delete_mem(object_id, test_token_manager.token)


@pytest.fixture()
def get_mem_endpoint():
    return GetMethod()


@pytest.fixture()
def delete_mem_endpoint():
    return DeleteMem()


@pytest.fixture()
def put_mem_endpoint():
    return PutMem()
