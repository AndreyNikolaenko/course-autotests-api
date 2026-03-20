from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.authentication.authentication_client import AuthenticationClient
from clients.users.public_users_client import PublicUsersClient
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from http import HTTPStatus
import pytest

@pytest.mark.regression
@pytest.mark.authentication
def test_login(public_users_client: PublicUsersClient,
               authentication_client: AuthenticationClient,
               function_user: UserFixture
               ):
    # public_users_client = get_public_users_client()
    # authentication_client = get_authentication_client()

    # create_user_request = CreateUserRequestSchema()
    # public_users_client.create_user(create_user_request)

    login_request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)



