from os import path

import allure
import pytest

from pages.store.catalog import CatalogPage


@allure.feature('Наличие элементов страницы')
@allure.title('Каталог товаров')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=25_28',
        'index.php?route=product/category&path=57',
        'index.php?route=product/category&path=24',
    ],
)
def test_elements(browser, page):
    browser.get(path.join(browser.current_url + page))
    catalog_page = CatalogPage(browser)
    elements_visible = [
        catalog_page.categories_side_menu.is_displayed(),
        catalog_page.grid_view_button.is_displayed(),
        catalog_page.list_view_button.is_displayed(),
        catalog_page.sort_select._el.is_displayed(),
        catalog_page.items_per_page_select._el.is_displayed(),
        catalog_page.cart_button.is_displayed(),
        catalog_page.menu.is_displayed(),
        catalog_page.top_search_button.is_displayed(),
        catalog_page.top_search_field.is_displayed(),
    ]
    expected = [True] * 9
    assert elements_visible == expected
    logs = catalog_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Сортировка товаров по названию в обратном порядке')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=24',
    ],
)
def test_name_sorting(browser, page):
    browser.get(path.join(browser.current_url + page))
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Name (Z - A)')
    products = catalog_page.get_product_names()
    assert products == sorted(products, reverse=True, key=str.casefold)
    logs = catalog_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Сортировка товаров по цене по возрастанию')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=24',
    ],
)
def test_price_sorting(browser, page):
    browser.get(path.join(browser.current_url + page))
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Price (Low > High)')
    products = catalog_page.get_product_prices()
    assert products == sorted(products)
    logs = catalog_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
