"""Тесты страницы Products"""
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.products_table import ProductsTable
from pages.admin.admin_base import AdminBasePage
from pages.admin.admin_products import AdminProductsPage


@pytest.fixture
def product_page(logged_admin_browser):
    """Переход на страницу Products"""
    logged_admin_browser.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(logged_admin_browser, 1).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    return logged_admin_browser


@pytest.mark.parametrize('keyword', ['ipod', 'iphone', 'samsung'])
def test_name_filter(product_page, keyword):
    """Проверка работы фильтра по имени товара"""
    product_page.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(product_page, 5).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    try:
        filter_button = WebDriverWait(product_page, 1).until(
            EC.visibility_of_element_located(AdminProductsPage.OPEN_FILTER_BUTTON)
        )
        filter_button.click()
    except TimeoutException:
        pass
    name_filter = product_page.find_element(*AdminProductsPage.NAME_FILTER)
    name_filter.send_keys(keyword)
    product_page.find_element(*AdminProductsPage.FILTER_BUTTON).click()
    table = ProductsTable(
        WebDriverWait(product_page, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        product_page,
    )
    products = table.get_column_values('Product Name')
    assert all(keyword in product.lower() for product in products)


def test_table_quantity_sorting(product_page):
    """ Проваерка работы сортировки по количеству товаров"""
    table = ProductsTable(
        WebDriverWait(product_page, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        product_page,
    )
    table.sort_by('Quantity')
    table = ProductsTable(
        WebDriverWait(product_page, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        product_page,
    )
    quantities = table.get_column_values('Quantity')
    assert quantities  # проверка на случай, если список вернётся пустым
    quantities = [int(quantity) for quantity in quantities]
    assert quantities == sorted(quantities, reverse=True)


def test_table_model_sorting(product_page):
    """ Проверка работы сортировки по названию модели"""
    table = ProductsTable(
        WebDriverWait(product_page, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        product_page,
    )
    table.sort_by('Model')
    table = ProductsTable(
        WebDriverWait(product_page, 10).until(
            EC.visibility_of_element_located(AdminProductsPage.PRODUCT_TABLE)
        ),
        product_page,
    )
    models = table.get_column_values('Model')
    assert models  # проверка на случай, если список вернётся пустым
    assert models == sorted(models, reverse=True, key=str.casefold)
