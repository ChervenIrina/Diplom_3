import allure
import pytest
from selenium import webdriver

from helpers_API import create_user, generate_new_user, delete_user


@pytest.fixture(scope='function')
@allure.title('Фикстура создает драйвер')
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
@allure.title('Фикстура создает/удаляет нового пользователя через API')
def new_user():
    payload = generate_new_user()
    user = create_user(payload)
    yield payload
    delete_user(user.json()["accessToken"])
