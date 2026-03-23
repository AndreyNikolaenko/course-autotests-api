import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response
from tools.fakers import fake

@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(email: str, public_users_client: PublicUsersClient):
    # public_users_client = get_public_users_client()

    generated_email = fake.email(domain = email)
    request = CreateUserRequestSchema(email=generated_email)
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # assert response.status_code == HTTPStatus.OK, 'Некорректный статус-код ответа'
    assert_status_code(response.status_code, HTTPStatus.OK)

    assert_create_user_response(request, response_data)
    # assert response_data.user.email == request.email, 'Некорректный e-mail пользователя'
    # assert response_data.user.last_name == request.last_name, 'Некорректный last_name пользователя'
    # assert response_data.user.first_name == request.first_name, 'Некорректный first_name пользователя'
    # assert response_data.user.middle_name == request.middle_name, 'Некорректный middle_name пользователя'

    validate_json_schema(response.json(), response_data.model_json_schema())
    print(response.json())
