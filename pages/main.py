from selenium.webdriver.common.by import By

from pages.store.base import StoreBasePage


class MainPage(StoreBasePage):
    FEATURED = (By.CSS_SELECTOR, '#content > div.row')
