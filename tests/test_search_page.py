from conftest import BASE_URL
from pages.store.search_results import SearchPage


def test_elements(browser):
    """Проверка наличия основных элементов страницы поиска"""
    browser.get(BASE_URL + 'index.php?route=product/search&search=Mac')
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
