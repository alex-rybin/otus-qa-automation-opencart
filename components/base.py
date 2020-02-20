from selenium.webdriver.remote import webdriver, webelement


class BaseComponent:
    def __init__(self, container: webelement, browser: webdriver):
        self.container = container
        self.browser = browser
