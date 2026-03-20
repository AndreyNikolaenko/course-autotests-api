import pytest

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из БД")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в БД")



@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    # @pytest.mark.usefixtures("clear_books_database", "fill_books_database")
    def test_read_books_from_library(self, fill_books_database, clear_books_database):
        pass

    # @pytest.mark.usefixtures("clear_books_database", "fill_books_database")
    def test_delete_books_from_library(self, fill_books_database, clear_books_database):
        pass


