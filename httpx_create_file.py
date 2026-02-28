import httpx

from tools.fakers import fake

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f"Create_user data: {create_user_response_data}\n")


login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f"Login data: {login_response_data}\n")


create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

create_file_response = httpx.post(
    'http://localhost:8000/api/v1/files',
    data={"filename": "images.png", "directory": "courses"},
    files= {"upload_file": open('./testdata/files/images.png', 'rb')},
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print(create_file_response.status_code)
print(create_file_response.content)
print(f"Create file response: {create_file_response_data}\n")



