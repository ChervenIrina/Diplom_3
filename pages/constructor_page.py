import allure

from constants import Url
from locators.constructor_page_locators import Locators as CPL
from locators.order_feed_page_locators import Locators as OFL
from locators.login_page_locators import Locators as LPL
from locators.base_page_locators import Locators as BPL
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Открываем страницу Конструктор(главная)')
    def go_to_site_main(self):
        self.go_to_site(Url.URL)

    @allure.step("Перетаскивание ингредиента в конструктор Бургера (Ингредиент задан по умолчанию)")
    def add_ingredient_to_order(self):
        self.wait_element(CPL.INGREDIENT_BUN)
        drag = self.find_element(CPL.INGREDIENT_BUN)
        drop = self.find_element(CPL.CONSTRUCTOR_BURGER_ORDER)
        self.drag_and_drop_element(drag, drop)

    @allure.step('Создание заказа')
    def create_order(self):
        self.click_element(CPL.CONSTRUCTOR_LABEL)
        self.add_ingredient_to_order()
        self.click_element(CPL.BUTTON_PLACE_AN_ORDER)

    @allure.step('Переход по клику из личного кабинета на страницу конструтор бургера')
    def go_to_page_constructor(self):
        self.click_element(LPL.PERSONAL_ACCOUNT)
        self.click_element(CPL.CONSTRUCTOR_LABEL)
        return self.get_element(CPL.CONSTRUCTOR_BURGER).is_displayed()

    @allure.step('Открытие формы "Детали игредиента"')
    def open_form_detail_ingredient(self):
        self.click_element(CPL.INGREDIENT_BUN)
        return self.get_element(BPL.FORM_DETAILS_OPEN).is_displayed()

    @allure.step('Закрытие формы "Детали ингердиента"')
    def close_form_detail_ingredient(self):
        self.click_element(CPL.INGREDIENT_BUN)
        self.click_element(BPL.BUTTON_CLOSE)
        return self.get_element(BPL.FORM_DETAILS_CLOSE).is_displayed()

    @allure.step('Получение кол-ва игредиентов в заказе')
    def counter_ingredient(self):
        return self.get_element(CPL.INGREDIENT_COUNTER).text

    @allure.step('Получение статуса заказа при успешном оформлении заказа')
    def order_status_progress(self):
        return self.get_element(CPL.LABEL_ORDERS).is_displayed()

    @allure.step('Получаем id заказа')
    def get_id_orders(self):
        self.wait_close_element(OFL.ICON_WAITING)
        self.wait_close_element(OFL.ICON_WAITING)
        return self.get_element(OFL.ORDER_ID).text
