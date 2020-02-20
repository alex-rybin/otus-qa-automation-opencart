import pytest
from selenium import webdriver

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
        help='Time in seconds for browser to implicitly wait for elements. Default: 0',
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
