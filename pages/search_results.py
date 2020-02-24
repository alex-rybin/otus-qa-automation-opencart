from selenium.webdriver.common.by import By

from pages.store.base import StoreBasePage


class SearchPage(StoreBasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#input-search')
    CATEGORY_SELECT = (By.CSS_SELECTOR, 'select[name="category_id"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#button-search')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
