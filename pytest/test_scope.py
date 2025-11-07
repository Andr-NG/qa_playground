import pytest
import uuid


@pytest.fixture(scope="session")
def generate_uuid():
    return uuid.uuid4()


def test_same_uuid_in_tests(generate_uuid):
    uuid1 = generate_uuid
    uuid2 = generate_uuid
    assert uuid1 == uuid2