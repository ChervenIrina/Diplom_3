import allure

from locators.base_page_locators import Locators as BPL
from locators.order_feed_page_locators import Locators as OFL
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def list_elements(self, locator):
        list_elements = []
        for element in locator:
            list_elements.append(element.text)
        return list_elements

    def close_form_order(self):
        self.wait_close_element(OFL.ICON_WAITING)
        self.wait_close_element(OFL.ICON_WAITING)
        self.get_element(BPL.BUTTON_CLOSE).is_displayed()
        self.click_element(BPL.BUTTON_CLOSE)
