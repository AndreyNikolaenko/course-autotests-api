from pydoc import resolve

import httpx
from httpx import request

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача123",
    "complited": False,
    "UserId": 2
}

response = httpx.post('https://jsonplaceholder.typicode.com/todos', json= data)

print(response.status_code)
#print(response.request.headers)
print(response.json())

data = {"username": "test_user", "password": "123456"}
response = httpx.post('https://httpbin.org/post', data = data)

print(response.status_code)
#print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get('https://httpbin.org/get', headers=headers)

print(response.request.headers)
print(response.json())


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1", params = params)

print(response.url)
print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post('https://httpbin.org/post', files=files)

print(response.json())

with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')

print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get('https://httpbin.org/get')
print(response.json())

try:
    response = client.get('https://jsonplaceholder.typicode.com/invalid-url')
    response.raise_for_status()
    print(response.status_code)
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = client.get('https://httpbin.org/delay/5', timeout=None)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени", {e})

