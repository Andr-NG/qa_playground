from python_basics.classes_library_manager import BankAccount
import pytest


@pytest.fixture
def provide_input(request: pytest.FixtureRequest):
    return request.param


@pytest.mark.parametrize("provide_input", [10, 100], indirect=True)
def test_valid_deposit(provide_input):
    account = BankAccount("Alice", 100)
    assert account.balance == 100
    mapping = {10: 110, 100: 200}

    account.deposit(amount=provide_input)
    if provide_input in mapping:
        assert account.balance == mapping[provide_input]
        account.withdraw(provide_input)


@pytest.mark.parametrize("name, balance", [("Ann", 100), ("Tim", -10)])
def test_not_enough_funds_and_invalid_input(name, balance):
    account = BankAccount(name)
    if balance < 0:
        with pytest.raises(TypeError):
            account.withdraw(balance)
    else:
        with pytest.raises(ValueError, match="Cannot withdraw. Not enough funds"):
            account.withdraw(balance)


@pytest.mark.parametrize("a", [1, 3])  # right - 1
@pytest.mark.parametrize("b", [2, 4])  # left - 2
def test_print_a_b(a, b):
    print(a, b)
    # 2-1
    # 2-3
    # 4-1
    # 4-3
