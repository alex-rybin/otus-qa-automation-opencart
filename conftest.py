import pytest
from envparse import env
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.admin.admin_base import AdminBasePage
from pages.admin.admin_login import AdminLoginPage

BASE_URL = 'http://127.0.0.1/'


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


@pytest.fixture
def browser(request):
    selected_browser = request.config.getoption('--browser')
    if selected_browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        browser = webdriver.Firefox(options=options)
    elif selected_browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
    else:
        raise ValueError(
            f'--browser option can only be "firefox" or "chrome", received "{selected_browser}"'
        )
    request.addfinalizer(browser.quit)
    browser.implicitly_wait(request.config.getoption('--time'))
    browser.get(request.config.getoption('--url'))
    return browser


@pytest.fixture
def logged_admin_browser(browser):
    """Открывает страницу входа администратора и логинится"""
    env.read_envfile()
    browser.get(BASE_URL + 'admin/')
    login_field = browser.find_element(*AdminLoginPage.USERNAME_FIELD)
    password_field = browser.find_element(*AdminLoginPage.PASSWORD_FIELD)
    login_button = browser.find_element(*AdminLoginPage.LOGIN_BUTTON)
    login_field.send_keys(env.str('OPENCART_LOGIN'))
    password_field.send_keys(env.str('OPENCART_PASSWORD'))
    login_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
    )
    return browser
