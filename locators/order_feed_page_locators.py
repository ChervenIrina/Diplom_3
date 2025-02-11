from selenium.webdriver.common.by import By


class Locators:
    # Лента заказов
    ONE_ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    LIST_HISTORY_ORDERS_USER = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]//p[contains(text(), '#')]")
    LIST_ORDERS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]//p[contains(text(), '#')]")
    ICON_WAITING = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")
    COUNT_ORDERS_ALL_TIME = (By.XPATH, ".//div[@class = 'undefined mb-15']/p[contains(@class,'OrderFeed_number')]")
    COUNT_ORDERS_TODAY = (By.XPATH, ".//div[3]/p[contains(@class,'OrderFeed_number')]")
    ORDER_STATUS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[@class= 'text text_type_digits-default mb-2']")
    ORDER_ID = (By.XPATH, "//h2[contains(@class , 'Modal_modal__title_shadow__3ikwq')]")