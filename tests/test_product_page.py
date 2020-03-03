import pytest

from conftest import BASE_URL
from pages.store.product import ProductPage


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/product&product_id=43',
        'index.php?route=product/product&product_id=40',
        'index.php?route=product/product&product_id=28',
        'index.php?route=product/product&product_id=30',
        'index.php?route=product/product&product_id=45',
    ],
)
def test_elements(browser, page):
    """Проверка наличия основных элементов страницы товара"""
    browser.get(BASE_URL + page)
    product_page = ProductPage(browser)
    elements_visible = [
        product_page.add_to_cart_button.is_displayed(),
        product_page.add_to_wishlist.is_displayed(),
        product_page.compare_button.is_displayed(),
        product_page.product_name.is_displayed(),
        product_page.quantity_input_field.is_displayed(),
        product_page.cart_button.is_displayed(),
        product_page.menu.is_displayed(),
        product_page.top_search_button.is_displayed(),
        product_page.top_search_field.is_displayed()
    ]
    expected = [True] * 9
    assert elements_visible == expected


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/product&product_id=43',
        'index.php?route=product/product&product_id=40',
        'index.php?route=product/product&product_id=28',
        'index.php?route=product/product&product_id=48',
        'index.php?route=product/product&product_id=45',
    ],
)
def test_alert_success_after_adding_to_cart(browser, page):
    """Проверка появления сообщения о добавлении продукта в корзину"""
    browser.get(BASE_URL + page)
    product_page = ProductPage(browser)
    product_page.add_to_cart_button.click()
    assert product_page.is_success_alert_present()


@pytest.mark.parametrize(
    'page',
    [
        'index.php?route=product/product&product_id=43',
        'index.php?route=product/product&product_id=40',
        'index.php?route=product/product&product_id=28',
        'index.php?route=product/product&product_id=48',
        'index.php?route=product/product&product_id=45',
    ],
)
def test_alert_success_after_adding_to_wishlist(browser, page):
    """Проверка появления сообщения о добавлении товара в список желаемого"""
    browser.get(BASE_URL + page)
    product_page = ProductPage(browser)
    product_page.add_to_wishlist.click()
    assert product_page.is_success_alert_present()
