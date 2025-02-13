import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем отображение элемента')
    def wait_element(self, locator, time=20):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

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

    @allure.step('Ищем элемент')
    def find_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, drag, drop):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()

    @allure.step('Получение адреса текущей страницы')
    def get_to_page(self):
        return self.driver.current_url

