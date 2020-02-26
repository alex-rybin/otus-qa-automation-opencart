import pytest

from conftest import BASE_URL
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
    browser.get(BASE_URL + page)
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
    browser.get(BASE_URL + page)
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Name (Z - A)')
    products = catalog_page.get_product_names()
    assert products == sorted(products, reverse=True, key=str.casefold)


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/category&path=20',
        'index.php?route=product/category&path=18',
        'index.php?route=product/category&path=24',
    ],
)
def test_price_sorting(browser, page):
    browser.get(BASE_URL + page)
    catalog_page = CatalogPage(browser)
    catalog_page.sort_select.select_by_visible_text('Price (Low > High)')
    products = catalog_page.get_product_prices()
    assert products == sorted(products)
