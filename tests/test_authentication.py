from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа логина юзера
from tools.assertions.authentication import assert_login_response




@pytest.mark.authentication
@pytest.mark.regression
def test_login(function_user: UserFixture, public_users_client: PublicUsersClient, authentication_client: AuthenticationClient):

    # Создание запроса на логин
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)

    # Выполнение аутентификации
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)

    # Используем функцию для проверки ответа при успешной авторизации
    assert_login_response(response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())

