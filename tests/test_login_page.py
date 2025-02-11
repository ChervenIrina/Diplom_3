import allure
import pytest
from locators.login_page_locators import Locators
from locators.constructor_page_locators import Locators as CPL
from locators.order_feed_page_locators import Locators as OPL
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from conftest import driver, new_user
from pages.order_feed_page import OrderFeedPage


class TestLoginPage:


    @allure.title('Проверка входа через кнопку "Личный кабинет"')
    def test_login_button_personal_account(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        lp.go_to_site()
        lp.click_element(Locators.PERSONAL_ACCOUNT)
        user_email = new_user['email']
        user_password = new_user['password']
        lp.set_user(user_email, user_password)
        lp.click_element(Locators.LOGIN_BUTTON)
        assert lp.get_element(Locators.MAIN_PAGE).is_displayed()

    @allure.title('Проверка истории заказов')
    def test_history_orders(self, driver, new_user):
        # авторизовались под новым пользователем
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        # создали заказ
        cp = ConstructorPage(driver)
        cp.click_element(CPL.CONSTRUCTOR_LABEL)
        cp.create_order()
        cp.wait_close_element(OPL.ICON_WAITING)
        # закрыли форму пользователя
        of = OrderFeedPage(driver)
        of.close_form_order()

        lp.click_element(Locators.PERSONAL_ACCOUNT)
        lp.click_element(Locators.HISTORY_ORDERS)
        assert lp.get_element(Locators.LIST_HISTORY_ORDERS).is_displayed()

    @allure.title('Проверка выхода из аккаунта')
    def test_logging_user(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        lp.click_element(Locators.PERSONAL_ACCOUNT)
        lp.click_element(Locators.EXIT_BUTTON)
        assert lp.get_element(Locators.LOGIN_BUTTON).is_displayed()
