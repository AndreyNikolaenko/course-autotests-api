from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from tools.fakers import fake
from clients.files.files_schema import FileSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
# from clients.users.private_users_client import User
from clients.users.users_schema import UserSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, \
    CreateCourseResponseSchema, UpdateCourseRequestSchema


# class Course(TypedDict):
#     """
#     Описание структуры курса
#     """
#     id: str
#     title: str
#     maxScore: int
#     minScore: int
#     description: str
#     previewFile: FileSchema
#     estimatedTime: str
#     createdByUser: UserSchema
#

# class CreateCourseResponse(TypedDict):
#     """
#     Описание структуры ответа создания курса.
#     """
#     course: Course
#
#
# class GetCoursesQueryDict(TypedDict):
#     """
#     Описание структуры запроса на получение списка курсов.
#     """
#     userId: str
#
#
# class CreateCourseRequestDict(TypedDict):
#         """
#         Описание структуры запроса на создание курса.
#         """
#         title: str
#         maxScore: int
#         minScore: int
#         description: str
#         estimatedTime: str
#         previewFileId: str
#         createdByUserId: str
#
#
# class UpdateCourseRequestDict(TypedDict):
#     """
#     Описание структуры запроса на обновление курса
#     """
#     title: str | None
#     maxScore: int | None
#     minScore: int | None
#     description: str | None
#     estimatedTime: str | None


class CourseClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод для получения списка курсов по идентификатору пользователя

        :param query: Словарь с userId.
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод для получения курса по идентификатору

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self,request:  CreateCourseRequestSchema)->Response:
        """
        Метод создания курса

        :param request:Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema)->Response:
        """
        Метод обновления курса

        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CourseClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CourseClient(client=get_private_http_client(user))