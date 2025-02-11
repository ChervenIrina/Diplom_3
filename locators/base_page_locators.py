from selenium.webdriver.common.by import By


class Locators:

    # Локаторы в окнах для логики восстановления пароля
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    FORM_DETAILS_OPEN = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    FORM_DETAILS_CLOSE = (By.XPATH, "//section[@class ='Modal_modal__P3_V5']")
    HISTORY_ORDERS = (By.LINK_TEXT, "История заказов")
    BUTTON_CLOSE = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
