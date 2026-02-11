import httpx

login_payload = {
    "email": "test@example.com",
    "password": "test"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_headers = {
    "Authorization": f"Bearer {login_response.json()['token']['accessToken']}"
}

response = httpx.get("http://localhost:8000/api/v1/users/me", headers=login_response_headers)

print(response.status_code)
print(response.json())