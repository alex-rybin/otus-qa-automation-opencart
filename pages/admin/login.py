import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement, webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.admin.base import AdminBasePage
from pages.base import BasePage


class AdminLoginPage(BasePage):
    """Страница входа в панель администратора"""

    USERNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block > a')
    HEADER_LOGO = (By.CSS_SELECTOR, '#header-logo')

    _username_field = None
    _password_field = None
    _login_button = None
    _forgot_password_link = None
    _header_logo = None

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('AdminLoginPage')
        self.logger.info('Login page initialized')

    @property
    def username_field(self) -> webelement:
        self.logger.debug('Initializing username field')
        if not self._username_field:
            self._username_field = self.browser.find_element(*self.USERNAME_FIELD)
        return self._username_field

    @property
    def password_field(self) -> webelement:
        self.logger.debug('Initializing password field')
        if not self._password_field:
            self._password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        return self._password_field

    @property
    def login_button(self) -> webelement:
        self.logger.debug('Initializing login button')
        if not self._login_button:
            self._login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        return self._login_button

    @property
    def forgot_password_link(self) -> webelement:
        self.logger.debug('Initializing forgot password link')
        if not self._forgot_password_link:
            self._forgot_password_link = self.browser.find_element(
                *self.FORGOT_PASSWORD_LINK
            )
        return self._forgot_password_link

    @property
    def header_logo(self) -> webelement:
        self.logger.debug('Initializing header logo')
        if not self._header_logo:
            self._header_logo = self.browser.find_element(*self.HEADER_LOGO)
        return self._header_logo

    def login(self, login: str, password: str):
        """Вход в панель администратора"""
        self.logger.info('Starting login')
        self.username_field.send_keys(login)
        self.password_field.send_keys(password)
        self.login_button.click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
        )
        self.logger.info('Successfully logged in')
