import allure

from locators.forgot_and_rest_password_locators import Locators as FPL
from locators.base_page_locators import Locators as BPL
from pages.base_page import BasePage
from constants import Url


class ForgotPasswordPage(BasePage):

    @allure.step ('Открываем страницу Авторизации')
    def go_to_site_login(self):
        self.driver.get(Url.URL_LOGIN)

    @allure.step('Переходим на страницу сброса пароля')
    def go_to_site_resset_password(self, email):
        self.go_to_site_login()
        self.click_element(FPL.LINK_FORGOT_PASSWORD)
        self.set_element(BPL.EMAIL, email)
        self.click_element(FPL.BUTTON_FORGOT)
        self.wait_element(FPL.BUTTON_SAVE)

