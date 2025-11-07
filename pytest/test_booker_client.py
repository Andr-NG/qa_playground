import pytest
from booker_client import Client
from unittest.mock import patch


@pytest.fixture
def api():
    yield Client("https://restful-booker.herokuapp.com")


@pytest.fixture
def provide_data(request: pytest.FixtureRequest):
    return request.param


@pytest.mark.parametrize(
    "provide_data", [{"username": "admin", "password": "password123"}], indirect=True
)
def test_get_token(api: Client, provide_data: dict):
    data = provide_data
    resp = api.create_token(creds=data)
    print(resp)
    assert resp
    assert "token" in resp


@pytest.mark.parametrize(
    "provide_data", [{"username": "admin", "password": "password123"}], indirect=True
)
def test_get_token_mocked(api: Client, provide_data: dict):
    data = provide_data
    api_client = api
    expected_resp = {"token": "mocked_token"}

    # booker_client.requests.post refers to the .py file itself from where the class is loaded
    with patch("booker_client.requests.post") as mock_post:
        mock_post.return_value.json.return_value = expected_resp
        mock_post.return_value.status_code = 201
        resp = api_client.create_token(data)
        assert resp == expected_resp
        mock_post.assert_called_once_with(
            url="https://restful-booker.herokuapp.com/auth",
            json=data
        )
