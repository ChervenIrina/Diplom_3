import allure
import pytest

from pages.forgot_and_reset_password import ForgotPasswordPage
from conftest import driver, new_user
from constants import Url
from pages.login_page import LoginPage


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_forgot_password(self, driver):
        lp = LoginPage(driver)
        lp.go_to_site_login()
        fp = ForgotPasswordPage(driver)
        site = fp.go_to_page_forgot_password()
        assert site == Url.URL_FORGOT_PASSWORD

    @allure.title('Проверка ввода email на странице восстановления пароля и перехода к странице сброса')
    def test_reset_password(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        site = fp.go_to_page_resset_password(new_user['email'])
        assert site == Url.URL_RESET_PASSWORD

    @allure.title('проверка скрытого пароля по умолчанию')
    def test_hidden_password(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        fp.go_to_page_resset_password(new_user['email'])
        assert fp.get_attribute_type_password() == 'password'

    @allure.title('проверка отображения пароля при нажатии на элесент "глаз"')
    def test_not_hidden_password_and_status_field(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        fp.go_to_page_resset_password(new_user['email'])
        fp.click_eye_element_password()
        assert fp.get_attribute_type_password() == 'text' and fp.get_status_password_active_and_focused() is True



