import pytest
import os


@pytest.fixture
def generate_int(request: pytest.FixtureRequest):
    return request.param


@pytest.mark.skipif(os.getenv("ENV") == "DEV", reason="Wrong ENV")
@pytest.mark.parametrize("dividend, divider", [(5, 5), (6, 6), (7, 4)])
def test_get_one_by_division(dividend: int, divider: int):
    if divider < dividend:
        pytest.skip(reason="Cannot run the test")
    assert dividend / divider == 1
