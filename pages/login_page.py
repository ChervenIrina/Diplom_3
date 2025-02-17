import allure

from constants import Url
from locators.base_page_locators import Locators as BPL
from locators.login_page_locators import Locators as LPL
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открываем страницу Авторизации')
    def go_to_site_login(self):
        self.go_to_site(Url.URL_LOGIN)

    @allure.step('Ввода данных пользователя')
    def set_user(self, email, password):
        self.set_element(BPL.EMAIL, email)
        self.set_element(BPL.PASSWORD, password)

    @allure.step('Авторизация нового созданного пользователя')
    def authorization_new_user(self, user):
        user_email = user['email']
        user_password = user['password']
        self.go_to_site(Url.URL)
        self.click_element(BPL.PERSONAL_ACCOUNT)
        self.set_user(user_email, user_password)
        self.click_element(LPL.LOGIN_BUTTON)

    @allure.step('Получаем текст кнопки')
    def get_text_button_place_order(self):
        self.wait_element(BPL.BUTTON_PLACE_ORDER)
        return self.get_element(BPL.BUTTON_PLACE_ORDER).text

    @allure.step('Смотрим историю заказов пользователя')
    def get_history_orders_user(self):
        self.click_element(BPL.PERSONAL_ACCOUNT)
        self.click_element(LPL.HISTORY_ORDERS)
        return self.get_element(LPL.LIST_HISTORY_ORDERS).is_displayed()

    @allure.step('Выходим из аккаунта пользователя')
    def exit_user(self):
        self.click_element(BPL.PERSONAL_ACCOUNT)
        self.click_element(LPL.EXIT_BUTTON)
        return self.get_element(LPL.LOGIN_BUTTON).is_displayed()

    @allure.step('Получение заказов из истории заказов пользователя')
    def get_id_orders_history_user(self):
        self.click_element(BPL.PERSONAL_ACCOUNT)
        self.click_element(LPL.HISTORY_ORDERS)
        return self.get_element(BPL.LIST_HISTORY_ORDERS_USER).text

