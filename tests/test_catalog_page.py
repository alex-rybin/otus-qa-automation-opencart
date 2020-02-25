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
        catalog_page.top_search_field.is_displayed()
    ]
    expected = [True] * 9
    assert elements_visible == expected
