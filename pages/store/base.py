from selenium.webdriver.common.by import By

from pages.base import BasePage


class StoreBasePage(BasePage):
    TOP_SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    TOP_SEARCH_BUTTON = (By.CSS_SELECTOR, '#search > span')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')
    MENU = (By.CSS_SELECTOR, '#menu')
