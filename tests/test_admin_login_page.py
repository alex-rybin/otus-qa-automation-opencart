from conftest import BASE_URL
from pages.admin.admin_login import AdminLoginPage


def test_elements(browser):
    """Проверка наличия основных элементов страницы входа администратора"""
    browser.get(BASE_URL + 'admin/')
    browser.find_element(*AdminLoginPage.USERNAME_FIELD)
    browser.find_element(*AdminLoginPage.PASSWORD_FIELD)
    browser.find_element(*AdminLoginPage.FORGOT_PASSWORD_LINK)
    browser.find_element(*AdminLoginPage.LOGIN_BUTTON)
    browser.find_element(*AdminLoginPage.HEADER_LOGO)
