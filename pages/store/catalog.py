from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.select import Select

from pages.store.base import StoreBasePage


class CatalogPage(StoreBasePage):
    SORT_SELECT = (By.CSS_SELECTOR, '#input-sort')
    ITEMS_PER_PAGE_SELECT = (By.CSS_SELECTOR, '#input-limit')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    CATEGORIES_SIDE_MENU = (By.CSS_SELECTOR, '#column-left > div:first-child')

    _sort_select = None
    _items_per_page_select = None
    _list_view_button = None
    _grid_view_button = None
    _categories_side_menu = None

    @property
    def sort_select(self) -> Select:
        if not self._sort_select:
            self._sort_select = Select(self.browser.find_element(*self.SORT_SELECT))
        return self._sort_select

    @property
    def items_per_page_select(self) -> Select:
        if not self._items_per_page_select:
            self._items_per_page_select = Select(
                self.browser.find_element(*self.ITEMS_PER_PAGE_SELECT)
            )
        return self._items_per_page_select

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

    @property
    def categories_side_menu(self) -> webelement:
        if not self._categories_side_menu:
            self._categories_side_menu = self.browser.find_element(
                *self.CATEGORIES_SIDE_MENU
            )
        return self._categories_side_menu
