import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver

from components.base import BaseComponent


class ProductsFilter(BaseComponent):
    """Фильтр на странице Products в панели администратора"""
    NAME_FILTER = (By.CSS_SELECTOR, '#input-name')
    MODEL_FILTER = (By.CSS_SELECTOR, '#input-model')
    PRICE_FILTER = (By.CSS_SELECTOR, '#input-price')
    QUANTITY_FILTER = (By.CSS_SELECTOR, '#input-quantity')
    STATUS_FILTER = (By.CSS_SELECTOR, '#input-status')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')

    _name_filter = None
    _model_filter = None
    _price_filter = None
    _quantity_filter = None
    _status_filter = None
    _filter_button = None

    def __init__(self, container: webelement, browser: webdriver):
        super().__init__(container=container, browser=browser)
        self.logger = logging.getLogger('opencart_logger')
        self.logger.debug('Products filter initialized')

    @property
    def name_filter(self) -> webelement:
        self.logger.debug('Initializing name filter field')
        if not self._name_filter:
            self._name_filter = self.container.find_element(*self.NAME_FILTER)
        return self._name_filter

    @property
    def model_filter(self) -> webelement:
        self.logger.debug('Initializing model filter field')
        if not self._model_filter:
            self._model_filter = self.container.find_element(*self.MODEL_FILTER)
        return self._model_filter

    @property
    def price_filter(self) -> webelement:
        self.logger.debug('Initializing price filter field')
        if not self._price_filter:
            self._price_filter = self.container.find_element(*self.PRICE_FILTER)
        return self._price_filter

    @property
    def quantity_filter(self) -> webelement:
        self.logger.debug('Initializing quantity filter field')
        if not self._quantity_filter:
            self._quantity_filter = self.container.find_element(*self.QUANTITY_FILTER)
        return self._quantity_filter

    @property
    def status_filter(self) -> webelement:
        self.logger.debug('Initializing status filter field')
        if not self._status_filter:
            self._status_filter = self.container.find_element(*self.STATUS_FILTER)
        return self._status_filter

    @property
    def filter_button(self) -> webelement:
        self.logger.debug('Initializing filter button')
        if not self._filter_button:
            self._filter_button = self.container.find_element(*self.FILTER_BUTTON)
        return self._filter_button

    def filter_by(self, by: str, value: str):
        self.logger.info(f'Filtering by {by} with value {value}')
        selected_filter = getattr(self, f'{by}_filter')
        selected_filter.clear()
        selected_filter.send_keys(value)
        self.filter_button.click()
