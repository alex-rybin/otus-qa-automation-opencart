import pytest
from selenium import webdriver

BASE_URL = 'http://127.0.0.1/'


def pytest_addoption(parser):
    parser.addoption(
        '-B',
        '--browser',
        action='store',
        default='firefox',
        help='Browser to use. Can be "firefox" or "chrome". Default: firefox',
    )
    parser.addoption(
        '-U',
        '--url',
        action='store',
        default=BASE_URL,
        help=f'URL to open for tests. Default: {BASE_URL}',
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
    browser.get(request.config.getoption('--url'))
    return browser
