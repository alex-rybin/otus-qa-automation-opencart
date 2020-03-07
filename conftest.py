import logging

import pytest
from envparse import env
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.admin.base import AdminBasePage
from pages.admin.login import AdminLoginPage

env.read_envfile()
BASE_URL = env.str('OPENCART_URL')


class EventListener(AbstractEventListener):
    def after_change_value_of(self, element, driver):
        logger.info(f'Changed value of {element}')

    def after_click(self, element, driver):
        logger.info(f'Clicked on {element}')

    def after_close(self, driver):
        logger.info(f'Closed window of {driver}')

    def after_execute_script(self, script, driver):
        logger.info(f'Executed script: {script}')

    def after_find(self, by, value, driver):
        logger.info(f'Searched {value} by {by}')

    def after_navigate_back(self, driver):
        logger.info('Navigated back')

    def after_navigate_forward(self, driver):
        logger.info('Navigated forward')

    def after_navigate_to(self, url, driver):
        logger.info(f'Opened URL: {url}')

    def after_quit(self, driver):
        logger.info('Browser quit')

    def before_change_value_of(self, element, driver):
        logger.info(f'Changing value of {element}')

    def before_click(self, element, driver):
        logger.info(f'Clicking on {element}')

    def before_close(self, driver):
        logger.info('Closing window')

    def before_execute_script(self, script, driver):
        logger.info(f'Executing script: {script}')

    def before_find(self, by, value, driver):
        logger.info(f'Searching {value} by {by}')

    def before_navigate_back(self, driver):
        logger.info('Navigating back')

    def before_navigate_forward(self, driver):
        logger.info('Navigating forward')

    def before_navigate_to(self, url, driver):
        logger.info(f'Opening URL: {url}')

    def before_quit(self, driver):
        logger.info('Quitting browser')

    def on_exception(self, exception, driver):
        logger.warning(f'Exception thrown: {exception}')


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


logging.basicConfig(
    format='[%(levelname)s] %(asctime)s: %(message)s', level=logging.INFO
)
logger = logging.getLogger('opencart_logger')


def finalizer(browser: webdriver):
    logger.info('Quit browser')
    browser.quit()


@pytest.fixture
def browser(request):
    selected_browser = request.config.getoption('--browser')
    if selected_browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        logger.info('Starting Firefox')
        browser = EventFiringWebDriver(
            webdriver.Firefox(options=options), EventListener()
        )
    elif selected_browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        logger.info('Starting Chrome')
        browser = EventFiringWebDriver(
            webdriver.Chrome(options=options), EventListener()
        )
    else:
        raise ValueError(
            f'--browser option can only be "firefox" or "chrome", received "{selected_browser}"'
        )
    request.addfinalizer(lambda: finalizer(browser))
    browser.implicitly_wait(request.config.getoption('--time'))
    browser.get(request.config.getoption('--url'))
    return browser


@pytest.fixture
def logged_admin_browser(browser):
    """Открывает страницу входа администратора и логинится"""
    browser.get(BASE_URL + 'admin/')
    login_page = AdminLoginPage(browser)
    login_page.login(env.str('OPENCART_LOGIN'), env.str('OPENCART_PASSWORD'))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
    )
    return browser
