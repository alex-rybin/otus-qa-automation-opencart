import re

from selenium.webdriver.common.by import By

from components.admin.side_menu import SideMenu
from pages.base import BasePage


class AdminBasePage(BasePage):
    """Базовый класс для описания страниц панели администратора"""

    SIDE_MENU = (By.CSS_SELECTOR, '#menu')

    _side_menu = None

    @property
    def side_menu(self) -> SideMenu:
        if not self._side_menu:
            self._side_menu = SideMenu(
                self.browser.find_element(*self.SIDE_MENU), self.browser
            )
        return self._side_menu

    def get_token(self) -> str:
        return re.search(r'user_token=(\w+)&?', self.browser.current_url).group(1)
