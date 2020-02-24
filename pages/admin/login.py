from selenium.webdriver.common.by import By
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

    def login(self, login: str, password: str):
        """Вход в панель администратора"""
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(login)
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
        )
