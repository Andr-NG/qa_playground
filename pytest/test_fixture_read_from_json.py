import pytest
import os
import json


@pytest.fixture
def read_json(request: pytest.FixtureRequest):
    with open(os.path.join(os.path.dirname(__file__), "..", request.param)) as file:
        return json.load(file)


@pytest.mark.parametrize("read_json", ["data.json"], indirect=True)
def test_json(read_json):
    assert read_json, "File reading failed"

    for el in read_json:
        assert el["username"]
        assert el["password"]
