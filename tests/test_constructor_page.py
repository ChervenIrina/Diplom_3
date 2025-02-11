import allure

from locators.constructor_page_locators import Locators as CPL
from locators.login_page_locators import Locators as LPL
from locators.base_page_locators import Locators as BPL
from pages.constructor_page import ConstructorPage
from conftest import driver, new_user
from pages.login_page import LoginPage


class TestConstructorPage:

    @allure.title('Проверка перехода по клику на «Конструктор» из личного кабинета')
    def test_click_on_constructor_label(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site()
        cp.click_element(LPL.PERSONAL_ACCOUNT)
        cp.click_element(CPL.CONSTRUCTOR_LABEL)
        assert cp.get_element(CPL.CONSTRUCTOR_BURGER).is_displayed()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site()
        cp.click_element(CPL.CONSTRUCTOR_ORDER_FEED)
        assert cp.get_element(CPL.TITLE_ORDER_FEED).is_displayed()

    @allure.title('Проверка клика на ингредиент (появится всплывающее окно с деталями)')
    def test_click_ingredient(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site()
        cp.click_element(CPL.INGREDIENT_BUN)
        assert cp.get_element(BPL.FORM_DETAILS_OPEN).is_displayed()

    @allure.title('Проверка закрытия всплывающего окна с деталями')
    def test_close_form_detail_ingredient(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site()
        cp.click_element(CPL.INGREDIENT_BUN)
        cp.click_element(BPL.BUTTON_CLOSE)
        assert cp.get_element(BPL.FORM_DETAILS_CLOSE)

    @allure.title('Проверка счетчика ингредиента при добавлении в заказ')
    def test_changing_counter_when_adding_ingredient_to_order(self, driver):
        cp = ConstructorPage(driver)
        cp.go_to_site()
        count_before = cp.get_element(CPL.INGREDIENT_COUNTER).text
        cp.add_ingredient_to_order(CPL.INGREDIENT_BUN)
        count_after = cp.get_element(CPL.INGREDIENT_COUNTER).text
        assert int(count_after) == int(count_before) + 2

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_creation(self, driver, new_user):
        lp = LoginPage(driver)
        lp.authorization_new_user(new_user)
        cp = ConstructorPage(driver)
        cp.create_order()
        assert cp.get_element(CPL.LABEL_ORDERS).is_displayed()

