from selenium.webdriver.common.by import By


class AdminLoginPage:
    USERNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '.help-block > a')
    HEADER_LOGO = (By.CSS_SELECTOR, '#header-logo')
