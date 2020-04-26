import logging
from datetime import datetime
from os import path

import pytest
from envparse import env
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.admin.base import AdminBasePage
from pages.admin.login import AdminLoginPage

env.read_envfile('.env.local')
BASE_URL = f'http://{env.str("OPENCART_HOST")}'


class EventListener(AbstractEventListener):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def after_change_value_of(self, element, driver):
        self.logger.info(f'Changed value of {element}')

    def after_click(self, element, driver):
        self.logger.info(f'Clicked on {element}')

    def after_close(self, driver):
        self.logger.info(f'Closed window of {driver}')

    def after_execute_script(self, script, driver):
        self.logger.info(f'Executed script: {script}')

    def after_find(self, by, value, driver):
        self.logger.info(f'Searched {value} by {by}')

    def after_navigate_back(self, driver):
        self.logger.info('Navigated back')

    def after_navigate_forward(self, driver):
        self.logger.info('Navigated forward')

    def after_navigate_to(self, url, driver):
        self.logger.info(f'Opened URL: {url}')

    def after_quit(self, driver):
        self.logger.info('Browser quit')

    def before_change_value_of(self, element, driver):
        self.logger.info(f'Changing value of {element}')

    def before_click(self, element, driver):
        self.logger.info(f'Clicking on {element}')

    def before_close(self, driver):
        self.logger.info('Closing window')

    def before_execute_script(self, script, driver):
        self.logger.info(f'Executing script: {script}')

    def before_find(self, by, value, driver):
        self.logger.info(f'Searching {value} by {by}')

    def before_navigate_back(self, driver):
        self.logger.info('Navigating back')

    def before_navigate_forward(self, driver):
        self.logger.info('Navigating forward')

    def before_navigate_to(self, url, driver):
        self.logger.info(f'Opening URL: {url}')

    def before_quit(self, driver):
        self.logger.info('Quitting browser')

    def on_exception(self, exception, driver):
        self.logger.warning(f'Exception thrown: {exception}')


def pytest_addoption(parser):
    parser.addoption(
        '-B',
        '--browser',
        action='store',
        default='firefox',
        help='Browser to use. Can be firefox or chrome. Default: firefox',
    )
    parser.addoption(
        '-U',
        '--url',
        action='store',
        default=BASE_URL,
        help=f'URL to open for tests. Default: {BASE_URL}',
    )
    parser.addoption(
        '-T',
        '--time',
        action='store',
        type=int,
        default=0,
        help='Time in seconds to implicitly wait for elements. Default: 0',
    )
    parser.addoption(
        '-F', '--file', action='store', type=str, default=None, help='Path to log file'
    )
    parser.addoption(
        '-E',
        '--executor',
        action='store',
        default=env.str('DEFAULT_HUB'),
        help='IP or domain of Selenium Hub',
    )


@pytest.fixture(scope='session')
def logger(request):
    logging.basicConfig(
        format='%(asctime)s %(name)s [%(levelname)s]: %(message)s',
        level=logging.INFO,
        filename=request.config.getoption('--file'),
        force=True,
    )
    return logging.getLogger('Fixture')


@pytest.fixture
def browser(logger, request):
    selected_browser = request.config.getoption('--browser')
    if selected_browser not in ('firefox', 'chrome'):
        raise ValueError(
            f'--browser option can only be "firefox" or "chrome", received "{selected_browser}"'
        )
    executor = request.config.getoption('--executor')
    browser_logger = logging.getLogger('Browser')
    logger.info(f'Starting {selected_browser.capitalize()}')
    browser = EventFiringWebDriver(
        webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            desired_capabilities={
                'browserName': selected_browser,
                'loggingPrefs': {'browser': 'ALL'},
                'acceptInsecureCerts': True,
            },
        ),
        EventListener(browser_logger),
    )
    browser.implicitly_wait(request.config.getoption('--time'))
    browser.get(request.config.getoption('--url'))
    failed = request.session.testsfailed
    yield browser
    if request.session.testsfailed > failed:
        browser.save_screenshot(
            f'screenshots/{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.png'
        )
    browser.quit()


@pytest.fixture
def logged_admin_browser(browser):
    """Открывает страницу входа администратора и логинится"""
    browser.get(path.join(browser.current_url, 'admin/'))
    login_page = AdminLoginPage(browser)
    login_page.login(env.str('OPENCART_LOGIN'), env.str('OPENCART_PASSWORD'))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
    )
    return browser
