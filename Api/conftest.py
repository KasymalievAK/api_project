import pytest
import requests

from dataclasses import dataclass
from Api.methods.authorize_methods import Authorize
from Api.methods.get_token_method import GetToken
from Api.methods.post_mem_method import PostMem
from Api.methods.get_mem_method import GetMethod
from Api.methods.delete_method import DeleteMem
from Api.methods.put_mem_method import PutMem
from Api.token_manipulations.check_token_status import TokenManager


@pytest.fixture()
def fix_authorize():
    return Authorize()


@dataclass
class TokenData:
    token: str
    another_token: str
    create_name: str


@pytest.fixture(scope="session")
def fix_test_token():
    manager = TokenManager()
    return manager.check_token()


@pytest.fixture()
def fix_get_token():
    return GetToken()


@pytest.fixture()
def fix_create_mem():
    return PostMem()


@dataclass
class MemData:
    object_id: int
    json_data: dict


@pytest.fixture()
def fix_test_mem(fix_create_mem, fix_test_token):
    data = {"text": "Мышь", "url": "https://cs18.pikabu.ru/s/2025/09/28/12/vnqrc5ru.webp",
            "tags": ['Ушастый'], "info": {"раздел": "Лига биологов"}}
    response, json_data = fix_create_mem.create_mem(data, fix_test_token.token)
    object_id = json_data['id']
    yield MemData(object_id=object_id, json_data=json_data)
    requests.delete(url=f'{fix_create_mem.url}/meme/{object_id}', headers=fix_create_mem._headers(fix_test_token.token))


@pytest.fixture()
def fix_get_mem():
    return GetMethod()


@pytest.fixture()
def fix_delete_mem():
    return DeleteMem()


@pytest.fixture()
def fix_put_mem():
    return PutMem()
