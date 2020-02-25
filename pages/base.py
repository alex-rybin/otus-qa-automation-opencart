from selenium.webdriver.remote import webdriver, webelement


class BasePage:
    """Базовый класс для описания страниц"""
    def __init__(self, browser: webdriver):
        self.browser = browser
