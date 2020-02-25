from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages.store.base import StoreBasePage


class MainPage(StoreBasePage):
    FEATURED = (By.CSS_SELECTOR, '#content > div.row')

    _featured = None

    @property
    def featured(self) -> webelement:
        if not self._featured:
            self._featured = self.browser.find_element(*self.FEATURED)
        return self._featured
