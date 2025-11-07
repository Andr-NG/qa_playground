from playwright.sync_api._generated import APIResponse
import pytest
from playwright.sync_api import sync_playwright, APIRequestContext


class APIClient:

    # APIRequestContext allows setting authorization headers that are shared accross all the calls
    # by using extra_http_headers

    def __init__(self, plawright_request: APIRequestContext):
        self.plawright_request = plawright_request

    def get(self, entity=None) -> APIResponse:
        if entity is None:
            URL = "/sim/entities"
        else:
            URL = f"/entities/{entity}"
        req = self.plawright_request.get(url=URL)
        return req

    def post(self, body: dict):
        req = self.plawright_request.post(
            url="/sim/entities", data=body, ignore_https_errors=True
        )
        return req


@pytest.fixture
def api():
    with sync_playwright() as f:  # can be replaced by the built-in playwright fixture
        # def api(playwright) -> playwright.request.new_context()
        play = f.request.new_context(
            ignore_https_errors=True, base_url="https://apichallenges.eviltester.com"
        )
        api: APIRequestContext = APIClient(plawright_request=play)
        yield api
        play.dispose()


def test_get_req(api: APIClient):
    response = api.get()
    print(response.json())
    assert response.status == 200


def test_post_req(api: APIClient):
    body = {"name": "bob"}
    response = api.post(body=body)
    print(response.json())
    assert response.status == 201
