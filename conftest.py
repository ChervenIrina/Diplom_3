import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service

from helpers_API import create_user, generate_new_user, delete_user


@pytest.fixture(params=["chrome", "firefox"])
@allure.title('Фикстура создает драйвер')
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
@allure.title('Фикстура создает/удаляет нового пользователя через API')
def new_user():
    payload = generate_new_user()
    user = create_user(payload)
    yield payload
    delete_user(user.json()["accessToken"])
