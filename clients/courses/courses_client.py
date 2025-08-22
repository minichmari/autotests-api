from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.files.files_client import File
from clients.users.users_schema import UserSchema


class Course(TypedDict):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: UserSchema

class GetCourserQueryDict(TypedDict):
    userId: str

class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class CreateCourseResponseDict(TypedDict):
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCourserQueryDict) -> Response:
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request:CreateCourseRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()

# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))