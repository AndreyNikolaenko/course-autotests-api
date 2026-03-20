import pytest
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_get_user_response
from clients.users.users_schema import GetUserResponseSchema
from clients.users.private_users_client import PrivateUsersClient

@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(private_users_client: PrivateUsersClient, function_user):
    response = private_users_client.get_user_me_api()

    assert_status_code(response.status_code, HTTPStatus.OK)

    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_get_user_response(response_data, function_user.response)


