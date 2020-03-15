from os import path

import pytest

from pages.store.catalog import CatalogPage


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
    """Проверка наличия основных элементов страницы каталога"""
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


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=24',
    ],
)
def test_name_sorting(browser, page):
    """Проверка сортировки товаров по названию в обратном порядке"""
    browser.get(path.join(browser.current_url + page))
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Name (Z - A)')
    products = catalog_page.get_product_names()
    assert products == sorted(products, reverse=True, key=str.casefold)
    logs = catalog_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=24',
    ],
)
def test_price_sorting(browser, page):
    """Проверка сортировки товаров по цене по возрастанию"""
    browser.get(path.join(browser.current_url + page))
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Price (Low > High)')
    products = catalog_page.get_product_prices()
    assert products == sorted(products)
    logs = catalog_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
