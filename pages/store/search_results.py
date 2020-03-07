import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.store.base import StoreBasePage


class SearchPage(StoreBasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#input-search')
    CATEGORY_SELECT = (By.CSS_SELECTOR, 'select[name="category_id"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#button-search')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    PRODUCT_NAMES = (By.CSS_SELECTOR, '#content > .row:nth-child(8) h4')

    _search_input = None
    _category_select = None
    _search_button = None
    _list_view_button = None
    _grid_view_button = None

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('opencart_logger')
        self.logger.info('Search results page initialized')

    @property
    def search_input(self) -> webelement:
        self.logger.debug('Initializing search input field')
        if not self._search_button:
            self._search_button = self.browser.find_element(*self.SEARCH_INPUT)
        return self._search_button

    @property
    def category_select(self) -> webelement:
        self.logger.debug('Initializing category select menu')
        if not self._category_select:
            self._category_select = self.browser.find_element(*self.CATEGORY_SELECT)
        return self._category_select

    @property
    def search_button(self) -> webelement:
        self.logger.debug('Initializing search button')
        if not self._search_button:
            self._search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        return self._search_button

    @property
    def list_view_button(self) -> webelement:
        self.logger.debug('Initializing list view button')
        if not self._list_view_button:
            self._list_view_button = self.browser.find_element(*self.LIST_VIEW_BUTTON)
        return self._list_view_button

    @property
    def grid_view_button(self) -> webelement:
        self.logger.debug('Initializing grid view button')
        if not self._grid_view_button:
            self._grid_view_button = self.browser.find_element(*self.GRID_VIEW_BUTTON)
        return self._grid_view_button

    def get_result_product_names(self) -> List[str]:
        self.logger.info('Getting product names from search results')
        results = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [result.text for result in results]
