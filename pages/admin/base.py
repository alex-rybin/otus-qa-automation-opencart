import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from components.admin.side_menu import SideMenu
from pages.base import BasePage


class AdminBasePage(BasePage):
    """Базовый класс для описания страниц панели администратора"""

    SIDE_MENU = (By.CSS_SELECTOR, '#menu')

    _side_menu = None

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('AdminBasePage')

    @property
    def side_menu(self) -> SideMenu:
        self.logger.debug('Initializing side menu')
        if not self._side_menu:
            self._side_menu = SideMenu(
                self.browser.find_element(*self.SIDE_MENU), self.browser
            )
        self.logger.info('Side menu initialized')
        return self._side_menu

    def get_token(self) -> str:
        self.logger.info('Getting user token')
        return re.search(r'user_token=(\w+)&?', self.browser.current_url).group(1)
