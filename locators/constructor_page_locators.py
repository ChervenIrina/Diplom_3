from selenium.webdriver.common.by import By


class Locators:

    # Локаторы старницы конструктор
    CONSTRUCTOR_LABEL = (By.LINK_TEXT, "Конструктор")
    CONSTRUCTOR_BURGER = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
    CONSTRUCTOR_ORDER_FEED = (By.LINK_TEXT, "Лента Заказов")
    TITLE_ORDER_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")
    INGREDIENT_BUN = (By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']")
    INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']/div/p")
    BUN_TOP = (By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']")
    CONSTRUCTOR_BURGER_ORDER = (By.XPATH, '/html/body/div/div/main/section[2]/ul/li[2]')
    BUTTON_PLACE_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    LABEL_ORDERS = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")