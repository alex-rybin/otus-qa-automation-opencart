import pytest
from envparse import env
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.products_table import ProductsTable
from conftest import BASE_URL
from pages.admin.admin_base import AdminBasePage
from pages.admin.admin_login import AdminLoginPage
from pages.admin.admin_products import AdminProductsPage


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


def test_name_filter(logged_admin_browser):
    filter_text = 'ipod'
    logged_admin_browser.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(logged_admin_browser, 1).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    name_filter = WebDriverWait(logged_admin_browser, 10).until(
        EC.visibility_of_element_located(AdminProductsPage.NAME_FILTER)
    )
    name_filter.send_keys(filter_text)
    logged_admin_browser.find_element(*AdminProductsPage.FILTER_BUTTON).click()
    table = ProductsTable(
        WebDriverWait(logged_admin_browser, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        logged_admin_browser,
    )
    products = table.get_column_values('Product Name')
    assert all(filter_text in product.lower() for product in products)
