import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')

    _add_to_cart_button = None
    _quantity_input_field = None
    _add_to_wishlist_button = None
    _compare_button = None
    _product_name = None

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('ProductPage')
        self.logger.info('Product store page initialized')

    @property
    def add_to_cart_button(self) -> webelement:
        self.logger.debug('Initializing add to cart button')
        if not self._add_to_cart_button:
            self._add_to_cart_button = self.browser.find_element(
                *self.ADD_TO_CART_BUTTON
            )
        return self._add_to_cart_button

    @property
    def quantity_input_field(self) -> webelement:
        self.logger.debug('Initializing quantity input field')
        if not self._quantity_input_field:
            self._quantity_input_field = self.browser.find_element(
                *self.QUANTITY_INPUT_FIELD
            )
        return self._quantity_input_field

    @property
    def add_to_wishlist(self) -> webelement:
        self.logger.debug('Initializing add to wishlist button')
        if not self._add_to_wishlist_button:
            self._add_to_wishlist_button = self.browser.find_element(
                *self.ADD_TO_WISHLIST_BUTTON
            )
        return self._add_to_wishlist_button

    @property
    def compare_button(self) -> webelement:
        self.logger.debug('Initializing compare button')
        if not self._compare_button:
            self._compare_button = self.browser.find_element(*self.COMPARE_BUTTON)
        return self._compare_button

    @property
    def product_name(self) -> webelement:
        self.logger.debug('Initializing product name')
        if not self._product_name:
            self._product_name = self.browser.find_element(*self.PRODUCT_NAME)
        return self._product_name

    def is_success_alert_present(self) -> bool:
        self.logger.info('Checking success alert presence')
        try:
            WebDriverWait(self.browser, 1).until(
                EC.visibility_of_element_located(self.ALERT_SUCCESS)
            )
            return True
        except TimeoutException:
            return False
