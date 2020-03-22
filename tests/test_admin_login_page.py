from os import path

import allure

from pages.admin.login import AdminLoginPage


@allure.feature('Наличие элементов страницы')
@allure.title('Вход администратора')
@allure.severity(allure.severity_level.CRITICAL)
def test_elements(browser):
    browser.get(path.join(browser.current_url, 'admin/'))
    page = AdminLoginPage(browser)
    elements_visible = [
        page.username_field.is_displayed(),
        page.password_field.is_displayed(),
        page.forgot_password_link.is_displayed(),
        page.login_button.is_displayed(),
        page.header_logo.is_displayed()
    ]
    expected = [True] * 5
    assert elements_visible == expected
    logs = page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
