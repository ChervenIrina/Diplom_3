import allure

from locators.base_page_locators import Locators as BPL
from locators.order_feed_page_locators import Locators as OFL
from locators.order_feed_page_locators import Locators as OPL
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Создание списка элементов')
    def list_elements(self, locator):
        list_elements = []
        for element in locator:
            list_elements.append(element.text)
        return list_elements

    @allure.step('Получение истории заказов')
    def get_id_orders_history(self):
        self.click_element(OFL.LABEL_ORDER_FEED)
        return self.list_elements(self.find_elements(OPL.LIST_ORDERS))

    @allure.step('Открытие формы "Заказ"')
    def open_form_order(self):
        self.click_element(OFL.LABEL_ORDER_FEED)
        self.click_element(OFL.ONE_ORDER)
        return self.get_element(BPL.FORM_DETAILS_OPEN).is_displayed()

    @allure.step('Закрытие формы "Заказ"')
    def close_form_order(self):
        self.wait_close_element(OFL.ICON_WAITING)
        self.wait_close_element(OFL.ICON_WAITING)
        self.get_element(BPL.BUTTON_CLOSE).is_displayed()
        self.click_element(BPL.BUTTON_CLOSE)

    @allure.step('Переход в ленту заказов')
    def go_to_page_order_feed(self):
        self.click_element(OFL.LABEL_ORDER_FEED)
        return self.get_element(OFL.TITLE_ORDER_FEED).is_displayed()

    @allure.step('Получаем кол-во всех выполненых заказов')
    def get_count_all_time_orders(self):
        self.click_element(OFL.LABEL_ORDER_FEED)
        return self.get_element(OPL.COUNT_ORDERS_ALL_TIME).text

    @allure.step('Получаем кол-во выполненых заказов за сегодня')
    def get_count_today_orders(self):
        self.click_element(OFL.LABEL_ORDER_FEED)
        return self.get_element(OPL.COUNT_ORDERS_TODAY).text

    @allure.step('Смотрим наш заказ "В работе"')
    def status_order(self):
        self.click_element(OPL.LABEL_ORDER_FEED)
        self.wait_element(OPL.ORDER_STATUS)
        self.wait_element(OPL.ORDER_STATUS)
        return self.get_element(OPL.ORDER_STATUS).text



