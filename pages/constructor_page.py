import allure

from locators.constructor_page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class ConstructorPage(BasePage):

    @allure.step("Перетаскивание ингредиента в конструктор Бургера")
    def add_ingredient_to_order(self, locator):
        self.wait_element(locator)
        drag = self.driver.find_element(*locator)
        drop = self.driver.find_element(*Locators.CONSTRUCTOR_BURGER_ORDER)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_ingredient_to_order(Locators.INGREDIENT_BUN)
        self.click_element(Locators.BUTTON_PLACE_AN_ORDER)
