from os import path

import allure
import pytest

from pages.store.product import ProductPage


@allure.feature('Наличие элементов страницы')
@allure.title('Страница товара')
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
    browser.get(path.join(browser.current_url + page))
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
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Появление сообщения о добавлении продукта в корзину')
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
    browser.get(path.join(browser.current_url + page))
    product_page = ProductPage(browser)
    product_page.add_to_cart_button.click()
    assert product_page.is_success_alert_present()
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Появление сообщения о добавлении товара в список желаемого')
@allure.severity(allure.severity_level.NORMAL)
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
    browser.get(path.join(browser.current_url + page))
    product_page = ProductPage(browser)
    product_page.add_to_wishlist.click()
    assert product_page.is_success_alert_present()
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
