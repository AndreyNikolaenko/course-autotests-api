import json
from textwrap import indent

json_data = """
{
  "name": "Иван",
  "last_name": "Иванов",
  "age": 25,
  "is_student": false,
  "courses": ["Python", "QA Automatoin", "API Testing",
    {
      "name": "Alise"
    }
  ],
  "address": {
    "city": "Москва",
    "zip": "123456"
  }
}
"""

#Делаем из строки(json) словарь и парсим по ключу
parsed_data = json.loads(json_data)

print(parsed_data['name'])
print(type(parsed_data), '\n')

data = {
    "name": "Семен",
    "last_name": "Семенов",
    "age": 20,
    "is_student": True
}
#Делаем из словаря json строку (сериализация)
json_str = json.dumps(data, indent = 4)

print(json_str, type(json_str), '\n')

#Читаем и присваиваем переменной json из файла
with open('json_example.json', 'r', encoding= 'utf-8') as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

#Создаем и записываем json в новый файл
with open('json_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent = 2, ensure_ascii= False)
