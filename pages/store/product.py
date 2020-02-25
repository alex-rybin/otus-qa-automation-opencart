from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.store.base import StoreBasePage


class ProductPage(StoreBasePage):
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

    _add_to_cart_button = None
    _quantity_input_field = None
    _add_to_wishlist_button = None
    _compare_button = None
    _product_name = None

    @property
    def add_to_cart_button(self) -> webelement:
        if not self._add_to_cart_button:
            self._add_to_cart_button = self.browser.find_element(*self.ADD_TO_CART_BUTTON)
        return self._add_to_cart_button

    @property
    def quantity_input_field(self) -> webelement:
        if not self._quantity_input_field:
            self._quantity_input_field = self.browser.find_element(*self.QUANTITY_INPUT_FIELD)
        return self._quantity_input_field

    @property
    def add_to_wishlist(self) -> webelement:
        if not self._add_to_wishlist_button:
            self._add_to_wishlist_button = self.browser.find_element(*self.ADD_TO_WISHLIST_BUTTON)
        return self._add_to_wishlist_button

    @property
    def compare_button(self) -> webelement:
        if not self._compare_button:
            self._compare_button = self.browser.find_element(*self.COMPARE_BUTTON)
        return self._compare_button

    @property
    def product_name(self) -> webelement:
        if not self._product_name:
            self._product_name = self.browser.find_element(*self.PRODUCT_NAME)
        return self._product_name
