import allure

from constants import Url
from locators.forgot_and_rest_password_locators import Locators as FPL
from locators.base_page_locators import Locators as BPL
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Переходим на страницу сброса пароля')
    def go_to_page_resset_password(self, email):
        self.go_to_site(Url.URL_LOGIN)
        self.click_element(FPL.LINK_FORGOT_PASSWORD)
        self.set_element(BPL.EMAIL, email)
        self.click_element(FPL.BUTTON_FORGOT)
        self.wait_element(FPL.BUTTON_SAVE)
        return self.get_to_page()

    @allure.step('Переход на страницу Восстановления пароля')
    def go_to_page_forgot_password(self):
        self.click_element(FPL.LINK_FORGOT_PASSWORD)
        return self.get_to_page()

    @allure.step('Получение атрибута типа поля Пароль')
    def get_attribute_type_password(self):
        return self.get_attribute_element(FPL.LABEL_NEW_PASSWORD, 'type')

    @allure.step('Получение статуса активности и фокуса поля Пароль')
    def get_status_password_active_and_focused(self):
        status = False
        if self.get_element(FPL.PASSWORD_ACTIVE).is_displayed() \
                and self.get_element(FPL.PASSWORD_FOCUSED).is_displayed():
            status = True
        return status

    @allure.step('Нажатие на элемент глаз в поле Пароль')
    def click_eye_element_password(self):
        self.click_element(FPL.ICON_PASSWORD_ACTION)
