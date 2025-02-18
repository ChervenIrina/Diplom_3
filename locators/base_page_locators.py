from selenium.webdriver.common.by import By


class Locators:

    # Локаторы
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    FORM_DETAILS_OPEN = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    FORM_DETAILS_CLOSE = (By.XPATH, "//section[@class ='Modal_modal__P3_V5']")
    HISTORY_ORDERS = (By.LINK_TEXT, "История заказов")
    BUTTON_CLOSE = (By.XPATH, ".//button[contains(@class, 'modal__close')]")
    BUTTON_PLACE_ORDER = (By.XPATH, ".//button[contains(@class, 'button_button__33qZ0') and text() = 'Оформить заказ']")
    ICON_WAITING = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")
    ORDER_ID = (By.XPATH, "//h2[contains(@class , 'Modal_modal__title_shadow__3ikwq')]")
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    LIST_HISTORY_ORDERS_USER = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]//p[contains(text(), '#')]")
