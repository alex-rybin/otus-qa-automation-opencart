from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


class LoginClientLibrary:
    EMAIL_FIELD = (By.ID, 'input-email')
    PASSWORD_FIELD = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    OPENCART_LOGIN_URL = (
        'http://otus-qa-automation-opencart_opencart_1/index.php?route=account/login'
    )

    def login_client(self, login: str, password: str, browser: webdriver):
        browser.get(self.OPENCART_LOGIN_URL)
        browser.find_element(*self.EMAIL_FIELD).send_keys(login)
        browser.find_element(*self.PASSWORD_FIELD).send_keys(password)
        browser.find_element(*self.LOGIN_BUTTON).click()
