from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    QUANTITY_INPUT_FIELD = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WISHLIST_BUTTON = (
        By.CSS_SELECTOR,
        '#content > div:first-child button[data-original-title="Add to Wish List"]',
    )
    COMPARE_BUTTON = (
        By.CSS_SELECTOR,
        '#content > div:first-child button[data-original-title="Compare this Product"]',
    )
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content h1')
