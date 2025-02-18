import allure
import pytest

from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from conftest import driver, new_user
from pages.login_page import LoginPage


class TestConstructorPage:

    @allure.title('Проверка перехода по клику на «Конструктор» из личного кабинета')
    def test_click_on_constructor_label(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        assert cp.go_to_page_constructor() is True

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        of = OrderFeedPage(driver)
        assert of.go_to_page_order_feed() is True

    @allure.title('Проверка клика на ингредиент (появится всплывающее окно с деталями)')
    def test_click_ingredient(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        assert cp.open_form_detail_ingredient() is True

    @allure.title('Проверка закрытия всплывающего окна с деталями')
    def test_close_form_detail_ingredient(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        assert cp.close_form_detail_ingredient() is True

    @allure.title('Проверка счетчика ингредиента при добавлении в заказ')
    def test_changing_counter_when_adding_ingredient_to_order(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site_main()
        count_before = cp.counter_ingredient()
        cp.add_ingredient_to_order()
        count_after = cp.counter_ingredient()
        assert int(count_after) == int(count_before) + 2

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_creation(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        cp = ConstructorPage(driver)
        cp.create_order()
        assert cp.order_status_progress() is True

