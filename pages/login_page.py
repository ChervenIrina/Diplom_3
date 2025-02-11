import allure

from locators.base_page_locators import Locators as BPL
from locators.login_page_locators import Locators as LPL
from pages.base_page import BasePage


class LoginPage(BasePage):


    @allure.step('Ввода данных пользователя')
    def set_user(self, email, password):
        self.set_element(BPL.EMAIL, email)
        self.set_element(BPL.PASSWORD, password)

    @allure.step('Авторизация нового созданного пользователя')
    def authorization_new_user(self, user):
        user_email = user['email']
        user_password = user['password']
        self.go_to_site()
        self.click_element(LPL.PERSONAL_ACCOUNT)
        self.set_user(user_email, user_password)
        self.click_element(LPL.LOGIN_BUTTON)

