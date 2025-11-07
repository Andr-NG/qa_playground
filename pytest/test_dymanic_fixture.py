import pytest
import os


file_1 = os.path.join(os.path.dirname(__file__), "..", "file_1.txt")
file_2 = os.path.join(os.path.dirname(__file__), "..", "file_2.txt")


@pytest.fixture
# request fixture is a special fixture providing information of the requesting test function.
def provide_number(request: pytest.FixtureRequest):
    return request.param


@pytest.fixture
def provide_txt(request):
    with open(request.param, "r") as file:
        yield file.read()


def is_even(number: int) -> bool:
    if number == 7:
        return True
    return number % 2 == 0


@pytest.mark.parametrize(
    "provide_number",
    # parameterized values can have markers
    [2, 4, 6, 12, pytest.param(7, marks=pytest.mark.xfail(reason="7 is odd", strict=True)), 8, 10],
    indirect=True,
)
def test_is_even(provide_number):
    """Parameterized test checking whether given number is even.
    Will fail due to pytest.param(7, marks=pytest.mark.xfail(reason="7 is odd", strict=True))
    and  if number == 7 return True

    Args:
        provide_number (fixture): _description_
    """
    num = provide_number
    assert is_even(num)


@pytest.mark.parametrize("provide_txt", [file_1, file_2], indirect=True)
def test_files(provide_txt):
    """Parameterized test checking that provided files are not empty

    Args:
        provide_txt (fixture): provides txt file names
    """
    assert len(provide_txt) > 0
