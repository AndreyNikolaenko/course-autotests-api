"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid
from dbm import error

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
from random import randrange


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_user_name(self) -> str:
        return f"{self.first_name} {self.last_name}"



class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "PlayWrigth"
    max_score: int = Field(alias="maxScore", default_factory=lambda: randrange(1, 100))
    min_score: int = Field(alias="minScore", default=100)
    description: str = "PlayWrigth course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id= "course-id",
    title= "PlayWrigth",
    maxScore= 100,
    minScore= 10,
    description= "PlayWrigth",
    previewFile= FileSchema(
        id='file-id',
        url='https://example.com/',
        directory='courses',
        filename='file.png'
    ),
    estimatedTime= "1 week",
    createdByUser=UserSchema(
        id= 'user-id',
        email= 'user@example.com',
        lastName= 'Bond',
        firstName= 'Zara',
        middleName='Alise'
    )
)
print(f'Course default model: {course_default_model.model_dump()}')


course_dict = {
    "id": "course-id",
    "title": "PlayWrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "PlayWrigth",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "courses",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id": "user-id",
    "email": "user@example.com",
    "lastName": "Bond",
    "firstName": "Zara",
    "middleName": "Alise"
    }
}

course_dict_model = CourseSchema(**course_dict)

print(f'Course dict model: {course_dict_model}')

course_json = """
{
    "id": "course-id",
    "title": "PlayWrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "PlayWrigth",
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "courses",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id": "user-id",
    "email": "user@example.com",
    "lastName": "Bond",
    "firstName": "Zara",
    "middleName": "Alise"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)

print(f'Course json model: {course_json_model.estimated_time}')

print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

user = UserSchema(
        id= 'user-id',
        email= 'test@exampse.com',
        lastName= 'Bond',
        firstName= 'Zara',
        middleName='Alise'
    )
print(user.get_user_name(), user.username)

try:
    file =FileSchema(
            id='file-id',
            url='https://example.com/',
            directory='courses',
            filename='file.png'
    )
    print(file)
except ValidationError as error:
    print(error)
    print(error.errors())