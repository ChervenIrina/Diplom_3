import allure

from locators.forgot_and_rest_password_locators import Locators as FPL
from pages.forgot_and_reset_password import ForgotPasswordPage
from conftest import driver, new_user
from constants import Url
from pages.login_page import LoginPage


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_forgot_password(self, driver):
        fp = ForgotPasswordPage(driver)
        fp.go_to_site_login()
        fp.click_element(FPL.LINK_FORGOT_PASSWORD)
        assert driver.current_url == Url.URL_FORGOT_PASSWORD

    @allure.title('Проверка ввода email на странице восстановления пароля и перехода к странице сброса')
    def test_reset_password(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        fp.go_to_site_resset_password(new_user['email'])
        assert driver.current_url == Url.URL_RESET_PASSWORD

    @allure.title('проверка скрытого паролья по умолчанию')
    def test_hidden_password(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        fp.go_to_site_resset_password(new_user['email'])
        assert fp.get_attribute_element(FPL.LABEL_NEW_PASSWORD, 'type') == 'password'

    @allure.title('проверка отображения пароля при нажатии на элесент "глаз"')
    def test_not_hidden_password(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        fp = ForgotPasswordPage(driver)
        fp.go_to_site_resset_password(new_user['email'])
        fp.click_element(FPL.ICON_PASSWORD_ACTION)
        assert fp.get_attribute_element(FPL.LABEL_NEW_PASSWORD, 'type') == 'text' \
               and fp.get_element(FPL.PASSWORD_ACTIVE).is_displayed() and fp.get_element(FPL.PASSWORD_FOCUSED).is_displayed()



