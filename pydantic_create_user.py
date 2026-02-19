import uuid
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    email: EmailStr
    password: str
    last_name: str= Field(alias='lastName')
    first_name: str= Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя
    """
    user: UserSchema