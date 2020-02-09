import pytest

from conftest import BASE_URL
from pages.catalog import CatalogPage


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
    browser.find_element(*CatalogPage.CATEGORIES_SIDE_MENU)
    browser.find_element(*CatalogPage.GRID_VIEW_BUTTON)
    browser.find_element(*CatalogPage.LIST_VIEW_BUTTON)
    browser.find_element(*CatalogPage.SORT_SELECT)
    browser.find_element(*CatalogPage.ITEMS_PER_PAGE_SELECT)
