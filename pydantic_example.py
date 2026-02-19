from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive')

user_data = {
    'id': 1,
    'name': 'Alise',
    'email': 'alise@example.com',
    'isActive': True
}

user = UserSchema(**user_data)
print(user.model_dump())


user = User(
    id="1123",
    name='Alise',
    email='alise@example.com',
    is_active=False,
    address=Address(city='San Francisco', zip_code='12345')
)

print(user.model_dump(), type(user.model_dump()))
print(user.model_dump_json(), type(user.model_dump_json()))

