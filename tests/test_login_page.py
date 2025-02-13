import allure
import pytest
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from conftest import driver, new_user
from pages.order_feed_page import OrderFeedPage


class TestLoginPage:


    @allure.title('Проверка входа через кнопку "Личный кабинет"')
    def test_login_button_personal_account(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        temp = lp.get_text_button_place_order()
        assert temp == 'Оформить заказ'

    @allure.title('Проверка истории заказов')
    def test_history_orders(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        cp = ConstructorPage(driver)
        cp.create_order()
        of = OrderFeedPage(driver)
        of.close_form_order()
        assert lp.get_history_orders_user() is True

    @allure.title('Проверка выхода из аккаунта')
    def test_logging_user(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        assert lp.exit_user() is True
