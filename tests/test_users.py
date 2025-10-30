from http import HTTPStatus
import pytest


from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
def test_create_user(domain: str, public_users_client: PublicUsersClient):
    email = fake.email(domain=domain)
    request = CreateUserRequestSchema(email=email)
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)


    assert_status_code(response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(private_users_client:PrivateUsersClient, function_user):
    response = private_users_client.get_user_me_api()

    assert_status_code(response.status_code, HTTPStatus.OK)
    #response_data = GetUserResponseSchema.model_validate(response.json())
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    # Проверяем корректность данных пользователя
    assert_get_user_response(response_data,function_user.response)

    # Дополнительно можно проверить валидацию схемы
    validate_json_schema(response.json(), response_data.model_json_schema())

