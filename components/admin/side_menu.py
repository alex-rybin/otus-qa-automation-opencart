import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver

from components.base import BaseComponent


class SideMenu(BaseComponent):
    """Боковое меню в панели администратора"""
    MENU_ELEMENTS = (By.CSS_SELECTOR, 'li')
    SUBSECTION_HEAD = (By.CSS_SELECTOR, 'a')
    SUB_ELEMENTS = (By.CSS_SELECTOR, 'ul > li')

    def __init__(self, container: webelement, browser: webdriver):
        super().__init__(container=container, browser=browser)
        self.logger = logging.getLogger('opencart_logger')
        self.logger.debug('Side menu initialized')

    def _click_menu_element(self, parent: webelement, element_name: str):
        """Поиск и клик по элементу меню"""
        self.logger.debug(f'Searching menu element: {element_name}')
        class_value = parent.get_attribute('class')
        if 'collapsed' in class_value:
            parent.find_element(*self.SUBSECTION_HEAD).click()
        elements = parent.find_elements(*self.SUB_ELEMENTS)
        for element in elements:
            if element.text == element_name:
                element.click()
                return element
        raise ValueError(f'Couldn\'t find element labeled "{element_name}"')

    def click_menu_element(self, *menu_path: str):
        """Поиск в меню нужного элемента по пути, указанному в menu_path"""
        message = ' > '.join(menu_path)
        self.logger.info(f'Searching path in menu: {message}')
        menu_path = list(menu_path)
        sub_element = self._click_menu_element(self.container, menu_path.pop(0))
        while len(menu_path) > 0:
            sub_element = self._click_menu_element(sub_element, menu_path.pop(0))
