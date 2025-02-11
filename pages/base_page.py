import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Url


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = Url.URL

    @allure.step('Открываем основную страницу сайта')
    def go_to_site(self):
        self.driver.get(self.url)

    @allure.step('Ожидаем отображение элемента')
    def wait_element(self, locator, time=20):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    #def wait_element_visibility(self, locator, time=20):


    @allure.step('Ожидание закрытия элемента')
    def wait_close_element(self, locator, time=20):
        WebDriverWait(self.driver, time).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Кликаем по элементу {locator}')
    def click_element(self, locator):
        self.wait_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Присваем значение "{text}" элементу "{locator}"')
    def set_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем аттрибуты элемента')
    def get_attribute_element(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Получаем  элемент')
    def get_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Ищем несколько элементов')
    def find_elements(self, locator):
        self.wait_element(locator)
        return self.driver.find_elements(*locator)

