import pytest


@pytest.fixture(autouse=True, scope='class')
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')

@pytest.fixture(scope='session')
def settings():

    print('[SESSION] инициализируем настройки автотеста')

@pytest.fixture(scope='class')
def user():
    print('[CLASS] создаем данные пользователя один раз на тестовый класс')

@pytest.fixture(scope='function')
def users_client(settings):
    print("[FUNCTION] создаем API клиент на каждый автотест" )




class TestUserFlow:
    def test_user_can_login(self, users_client, user, settings):
        pass

    def test_user_can_create_course(self, users_client, user, settings):
        pass


class TestAccountFlow:
    def test_user_account(self, users_client, user, settings):
        pass

@pytest.fixture
def user_data() -> dict:
    print('Создаем пользователя до теста (setup)')
    yield {"user_name": "test_user", "email": "test@example.com", "password": "<PASSWORD>"}
    print('Удаляем пользователя после теста (teardown)')

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == 'test@example.com'

def test_user_name(user_data: dict):
    print(user_data)
    assert user_data["user_name"] == 'test_user'