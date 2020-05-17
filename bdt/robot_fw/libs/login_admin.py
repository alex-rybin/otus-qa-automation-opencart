from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


class LoginAdminLibrary:
    USERNAME_FIELD = (By.ID, 'input-username')
    PASSWORD_FIELD = (By.ID, 'input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    OPENCART_ADMIN_URL = 'http://otus-qa-automation-opencart_opencart_1/admin/'

    def login_admin(self, login: str, password: str, browser: webdriver):
        browser.get(self.OPENCART_ADMIN_URL)
        browser.find_element(*self.USERNAME_FIELD).send_keys(login)
        browser.find_element(*self.PASSWORD_FIELD).send_keys(password)
        browser.find_element(*self.SUBMIT_BUTTON).click()
