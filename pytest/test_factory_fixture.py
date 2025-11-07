from typing import Callable
import pytest


@pytest.fixture
def factory_fixture() -> Callable[..., dict]:
    def user_factory(count) -> dict:
        temp = {}
        for id in range(1, count+1):
            temp[id] = f"User{id}"
        return temp
    return user_factory


def test_print_user_dict(factory_fixture):

    dict_user = factory_fixture(10)
    for k, v in dict_user.items():
        print(v)
        assert isinstance(k, int)
        assert v.startwith("User")
