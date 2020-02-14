import pytest

from conftest import BASE_URL
from pages.product import ProductPage


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/product&product_id=43',
        'index.php?route=product/product&product_id=40',
        'index.php?route=product/product&product_id=42',
        'index.php?route=product/product&product_id=30',
        'index.php?route=product/product&product_id=45',
    ],
)
def test_elements(browser, page):
    """Проверка наличия основных элементов страницы товара"""
    browser.get(BASE_URL + page)
    browser.find_element(*ProductPage.ADD_TO_CART_BUTTON)
    browser.find_element(*ProductPage.ADD_TO_WISHLIST_BUTTON)
    browser.find_element(*ProductPage.COMPARE_BUTTON)
    browser.find_element(*ProductPage.PRODUCT_NAME)
    browser.find_element(*ProductPage.QUANTITY_INPUT_FIELD)
    browser.find_element(*ProductPage.CART_BUTTON)
    browser.find_element(*ProductPage.MENU)
    browser.find_element(*ProductPage.TOP_SEARCH_BUTTON)
    browser.find_element(*ProductPage.TOP_SEARCH_FIELD)
