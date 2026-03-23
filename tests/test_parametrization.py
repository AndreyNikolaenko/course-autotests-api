import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number",  [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected",  [(1, 1), (2, 5), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com",
])
def test_multiple_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com",
])
def host(request: SubRequest) -> str :
    return request.param

def test_host(host: str):
    print(f"Running host test: {host}")


@pytest.mark.parametrize("user", ["Alise", "Zara"])
class TestOperations:
    def test_user_with_operation(self, user: str):
        print(f"User with operation {user}")

    def test_user_without_operation(self, user: str):
        print(f"User without operation {user}")



users = {
    "+78008008080" : "User_1",
    "+78008008090" : "User_2",
    "+78008008070" : "User_3"
}



@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids = lambda phone_number: f"{phone_number}-{users[phone_number]}"
)
def test_identifiers(phone_number):
    pass

@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass

@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1