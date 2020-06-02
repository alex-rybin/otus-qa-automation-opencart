from robot.api.deco import keyword
from selenium import webdriver

from login_admin import LoginAdminLibrary
from login_client import LoginClientLibrary


class LoginLibrary:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    EXECUTOR = 'localhost'
    browser = None

    @keyword('Открыть браузер')
    def open_browser(self):
        if not self.browser:
            self.browser = webdriver.Remote(
                command_executor=f'http://{self.EXECUTOR}:4444/wd/hub',
                desired_capabilities={
                    'browserName': 'firefox',
                    'loggingPrefs': {'browser': 'ALL'},
                    'acceptInsecureCerts': True,
                },
            )
        return self.browser

    @keyword('Войти в админку')
    def login_admin(self, login: str, password: str):
        LoginAdminLibrary().login_admin(login, password, self.browser)

    @keyword('Войти в аккаунт пользователя')
    def login_client(self, login: str, password: str):
        LoginClientLibrary().login_client(login, password, self.browser)

    @keyword('Заголовок должен быть')
    def check_title(self, title: str):
        assert title == self.browser.title

    @keyword
    def close_browser(self):
        self.browser.close()
        self.browser = None
