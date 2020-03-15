import logging
from typing import List

from selenium.webdriver.remote import webdriver


class BasePage:
    """Базовый класс для описания страниц"""
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.logger = logging.getLogger('BasePage')
        self.logger.info('Base page initialized')

    def get_console_log(self) -> List[dict]:
        self.logger.info('Getting browser console log')
        if self.browser.name == 'chrome':
            return self.browser.get_log('browser')
        else:
            self.logger.warning('Only Chrome supports console log collection, returning empty list')
            return []
