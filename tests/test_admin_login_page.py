from conftest import BASE_URL
from pages.admin.login import AdminLoginPage


def test_elements(browser):
    """Проверка наличия основных элементов страницы входа администратора"""
    browser.get(BASE_URL + 'admin/')
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
