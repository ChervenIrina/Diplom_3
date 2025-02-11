import allure
import pytest

from locators.login_page_locators import Locators as LPL
from locators.order_feed_page_locators import Locators as OPL
from locators.base_page_locators import Locators as BPL
from locators.constructor_page_locators import Locators as CPL
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from conftest import driver, new_user


class TestOrderFeedPage:

    @allure.title('Проверка клика на заказ (откроется всплывающее окно с деталями)')
    def test_click_order(self, driver):
        of = OrderFeedPage(driver)
        of.go_to_site()
        of.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        of.click_element(OPL.ONE_ORDER)
        assert of.get_element(BPL.FORM_DETAILS_OPEN).is_displayed()

    @allure.title('Проверка на отображение закозов из Истории заказов пользователя в Ленты закзов')
    def test_user_orders_in_orders_feed(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)

        cp = ConstructorPage(driver)
        cp.create_order()

        of = OrderFeedPage(driver)
        of.close_form_order()
        of.click_element(LPL.PERSONAL_ACCOUNT)
        of.click_element(LPL.HISTORY_ORDERS)
        order_user = of.get_element(OPL.LIST_HISTORY_ORDERS_USER).text

        of.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        orders_list = of.list_elements(cp.find_elements(OPL.LIST_ORDERS))
        assert order_user in orders_list

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа ')
    def test_count_orders_all_time(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)

        lp.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        count_orders_before = lp.get_element(OPL.COUNT_ORDERS_ALL_TIME).text

        cp = ConstructorPage(driver)
        cp.click_element(CPL.CONSTRUCTOR_LABEL)
        cp.create_order()

        of = OrderFeedPage(driver)
        of.close_form_order()
        of.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        count_orders_after = lp.get_element(OPL.COUNT_ORDERS_ALL_TIME).text
        assert int(count_orders_after) == int(count_orders_before) + 1

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа ')
    def test_count_orders_today(self, driver, new_user):

        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)

        lp.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        count_orders_before = lp.get_element(OPL.COUNT_ORDERS_TODAY).text

        cp = ConstructorPage(driver)
        cp.click_element(CPL.CONSTRUCTOR_LABEL)
        cp.create_order()

        of = OrderFeedPage(driver)
        of.close_form_order()
        of.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        count_orders_after = lp.get_element(OPL.COUNT_ORDERS_TODAY).text
        assert int(count_orders_after) == int(count_orders_before) + 1

    @allure.title('Проверка заказа "В работе" после оформления заказа')
    def test_orders_status(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)

        cp = ConstructorPage(driver)
        cp.click_element(CPL.CONSTRUCTOR_LABEL)
        cp.create_order()

        cp.wait_close_element(OPL.ICON_WAITING)
        cp.wait_close_element(OPL.ICON_WAITING)

        order_id = cp.get_element(OPL.ORDER_ID).text
        cp.get_element(BPL.BUTTON_CLOSE).is_displayed()
        cp.click_element(BPL.BUTTON_CLOSE)

        of = OrderFeedPage(driver)
        of.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        of.wait_element(OPL.ORDER_STATUS)
        order_status = of.get_element(OPL.ORDER_STATUS).text
        assert '0'+order_id == order_status
