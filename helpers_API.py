import allure
import random
import string

import requests

from constants import Url

@allure.step('Создаем пользователя (рандомные данные)')
def generate_new_user():
    name = generate_random_string(10)
    email = f"{name}@yandex.ru"
    password = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

@allure.step('Генерация случай строки (ТД)')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Создаем нового пользователя')
def create_user(payload):
    response = requests.post(Url.NEW_USER, data=payload)
    return response

@allure.step('Удаляем пользователя')
def delete_user(token):
    response = requests.delete(Url.NEW_USER, data=token)
    return response

@allure.step('Авторизация пользователя')
def login_user(payload):
    response = requests.post(Url.USER_LOGIN, data=payload)
    return response