from selenium.webdriver.common.by import By


class Locators:
    # состояние элемента "ввода пароля" при активносте и фокусе
    LINK_FORGOT_PASSWORD = (By.LINK_TEXT, "Восстановить пароль")
    PASSWORD_ACTIVE = (By.XPATH, ".//div[contains(@class,'input_status_active')]")
    PASSWORD_FOCUSED = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")
    BUTTON_FORGOT = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    BUTTON_SAVE = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    ICON_PASSWORD_ACTION = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    LABEL_NEW_PASSWORD = (By.NAME, "Введите новый пароль")