from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа логина юзера
from tools.assertions.authentication import assert_login_response




@pytest.mark.authentication
@pytest.mark.regression
def test_login():
    # Инициализация клиентов
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # Создание пользователя
    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    # Создание запроса на логин
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    # Выполнение аутентификации
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)

    # Используем функцию для проверки ответа при успешной авторизации
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())

