from selenium.webdriver.common.by import By


class Locators:
    # Лента заказов
    ONE_ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")

    LIST_ORDERS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]//p[contains(text(), '#')]")

    COUNT_ORDERS_ALL_TIME = (By.XPATH, ".//div[@class = 'undefined mb-15']/p[contains(@class,'OrderFeed_number')]")
    COUNT_ORDERS_TODAY = (By.XPATH, ".//div[3]/p[contains(@class,'OrderFeed_number')]")
    ORDER_STATUS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[@class= 'text text_type_digits-default mb-2']")

    LABEL_ORDER_FEED = (By.LINK_TEXT, "Лента Заказов")
    TITLE_ORDER_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")