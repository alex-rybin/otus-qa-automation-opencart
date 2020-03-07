import logging

from selenium.webdriver.remote import webdriver


class BasePage:
    """Базовый класс для описания страниц"""
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.logger = logging.getLogger('opencart_logger')
        self.logger.info('Base page initialized')
