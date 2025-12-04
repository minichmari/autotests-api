from http import HTTPStatus
import pytest
import allure
from allure_commons.types import Severity

from clients.authentication.authentication_client import  AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа логина юзера
from tools.assertions.authentication import assert_login_response




@pytest.mark.regression
@pytest.mark.authentication
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Login with correct login and password")
    def test_login(self,function_user: UserFixture, authentication_client: AuthenticationClient):

        # Создание запроса на логин
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)

        # Выполнение аутентификации
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        # Используем функцию для проверки ответа при успешной авторизации
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

