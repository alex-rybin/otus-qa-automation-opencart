from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.base import BasePage


class StoreBasePage(BasePage):
    TOP_SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    TOP_SEARCH_BUTTON = (By.CSS_SELECTOR, '#search > span')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')
    MENU = (By.CSS_SELECTOR, '#menu')

    _top_search_field = None
    _top_search_button = None
    _cart_button = None
    _menu = None

    @property
    def top_search_field(self) -> webelement:
        if not self._top_search_field:
            self._top_search_field = self.browser.find_element(*self.TOP_SEARCH_FIELD)
        return self._top_search_field

    @property
    def top_search_button(self) -> webelement:
        if not self._top_search_button:
            self._top_search_button = self.browser.find_element(*self.TOP_SEARCH_BUTTON)
        return self._top_search_button

    @property
    def cart_button(self) -> webelement:
        if not self._cart_button:
            self._cart_button = self.browser.find_element(*self.CART_BUTTON)
        return self._cart_button

    @property
    def menu(self) -> webelement:
        if not self._menu:
            self._menu = self.browser.find_element(*self.MENU)
        return self._menu
