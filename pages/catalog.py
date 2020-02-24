from selenium.webdriver.common.by import By

from pages.store.base import StoreBasePage


class CatalogPage(StoreBasePage):
    SORT_SELECT = (By.CSS_SELECTOR, '#input-sort')
    ITEMS_PER_PAGE_SELECT = (By.CSS_SELECTOR, '#input-limit')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    CATEGORIES_SIDE_MENU = (By.CSS_SELECTOR, '#column-left > div:first-child')
