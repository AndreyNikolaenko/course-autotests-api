import httpx

login_payload = {
    "email": "test@example.com",
    "password": "test"
}
response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

auth_token = response.json()['token']['accessToken']

response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {auth_token}"})

print(response.status_code)
print(response.json())