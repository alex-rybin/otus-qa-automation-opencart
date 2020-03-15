import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver

from pages.store.base import StoreBasePage


class MainPage(StoreBasePage):
    FEATURED = (By.CSS_SELECTOR, '#content > div.row')

    _featured = None

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('MainPage')
        self.logger.info('Main store page initialized')

    @property
    def featured(self) -> webelement:
        self.logger.debug('Initializing featured block')
        if not self._featured:
            self._featured = self.browser.find_element(*self.FEATURED)
        return self._featured
