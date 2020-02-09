from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search > span')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')
    MENU = (By.CSS_SELECTOR, '#menu')
    FEATURED = (By.CSS_SELECTOR, '#content > div.row')
