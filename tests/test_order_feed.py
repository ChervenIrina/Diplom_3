import allure
import pytest

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from conftest import driver, new_user


class TestOrderFeedPage:

    @allure.title('Проверка клика на заказ (откроется всплывающее окно с деталями)')
    def test_click_order(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        of = OrderFeedPage(driver)
        assert of.open_form_order() is True

    @allure.title('Проверка на отображение закозов из Истории заказов пользователя в Ленты закзов')
    def test_user_orders_in_orders_feed(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        cp = ConstructorPage(driver)
        cp.create_order()
        of = OrderFeedPage(driver)
        of.close_form_order()
        order_user = lp.get_id_orders_history_user()
        orders_list = of.get_id_orders_history()
        assert order_user in orders_list

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа ')
    def test_count_orders_all_time(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        of = OrderFeedPage(driver)
        count_orders_before = int(of.get_count_all_time_orders())
        cp = ConstructorPage(driver)
        cp.create_order()
        of.close_form_order()
        count_orders_after = int(of.get_count_all_time_orders())
        assert count_orders_after == count_orders_before + 1

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа ')
    def test_count_orders_today(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        of = OrderFeedPage(driver)
        count_orders_before = int(of.get_count_today_orders())
        cp = ConstructorPage(driver)
        cp.create_order()
        of.close_form_order()
        count_orders_after = int(of.get_count_today_orders())
        assert count_orders_after == count_orders_before + 1

    @allure.title('Проверка заказа "В работе" после оформления заказа')
    def test_orders_status(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        cp = ConstructorPage(driver)
        cp.create_order()
        order_id = cp.get_id_orders()
        of = OrderFeedPage(driver)
        of.close_form_order()
        order_status = of.status_order()
        assert '0' + order_id == order_status
