from selenium.webdriver.common.by import By


class Locators:
    # Локаторы Личного кабинета
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    HISTORY_ORDERS = (By.LINK_TEXT, "История заказов")
    LIST_HISTORY_ORDERS = (By.XPATH, ".//div[contains(@class, 'OrderHistory_orderHistory')]")
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")