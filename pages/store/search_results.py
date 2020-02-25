from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.store.base import StoreBasePage


class SearchPage(StoreBasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#input-search')
    CATEGORY_SELECT = (By.CSS_SELECTOR, 'select[name="category_id"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#button-search')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')

    _search_input = None
    _category_select = None
    _search_button = None
    _list_view_button = None
    _grid_view_button = None

    @property
    def search_input(self) -> webelement:
        if not self._search_button:
            self._search_button = self.browser.find_element(*self.SEARCH_INPUT)
        return self._search_button

    @property
    def category_select(self) -> webelement:
        if not self._category_select:
            self._category_select = self.browser.find_element(*self.CATEGORY_SELECT)
        return self._category_select

    @property
    def search_button(self) -> webelement:
        if not self._search_button:
            self._search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        return self._search_button

    @property
    def list_view_button(self) -> webelement:
        if not self._list_view_button:
            self._list_view_button = self.browser.find_element(*self.LIST_VIEW_BUTTON)
        return self._list_view_button

    @property
    def grid_view_button(self) -> webelement:
        if not self._grid_view_button:
            self._grid_view_button = self.browser.find_element(*self.GRID_VIEW_BUTTON)
        return self._grid_view_button
