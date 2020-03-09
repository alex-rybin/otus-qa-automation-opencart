import pytest

from pages.store.main import MainPage
from pages.store.search_results import SearchPage


def test_elements(browser):
    """Проверка наличия основных элементов страницы поиска"""
    browser.get(browser.current_url + 'index.php?route=product/search&search=Mac')
    page = SearchPage(browser)
    elements_visible = [
        page.search_button.is_displayed(),
        page.grid_view_button.is_displayed(),
        page.list_view_button.is_displayed(),
        page.category_select.is_displayed(),
        page.search_input.is_displayed(),
        page.cart_button.is_displayed(),
        page.menu.is_displayed(),
        page.top_search_button.is_displayed(),
        page.top_search_field.is_displayed(),
    ]
    expected = [True] * 9
    assert elements_visible == expected
    logs = page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@pytest.mark.parametrize('keyword', ['ipod', 'macbook'])
def test_search(browser, keyword):
    """Проверка корректности работы поиска по товарам"""
    page = MainPage(browser)
    page.search(keyword)
    page = SearchPage(browser)
    results = page.get_result_product_names()
    assert all(keyword in result.lower() for result in results)
    logs = page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
