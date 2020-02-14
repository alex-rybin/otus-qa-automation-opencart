from conftest import BASE_URL
from pages.search_results import SearchPage


def test_elements(browser):
    """Проверка наличия основных элементов страницы поиска"""
    browser.get(BASE_URL + 'index.php?route=product/search&search=Mac')
    browser.find_element(*SearchPage.SEARCH_BUTTON)
    browser.find_element(*SearchPage.GRID_VIEW_BUTTON)
    browser.find_element(*SearchPage.LIST_VIEW_BUTTON)
    browser.find_element(*SearchPage.CATEGORY_SELECT)
    browser.find_element(*SearchPage.SEARCH_INPUT)
    browser.find_element(*SearchPage.CART_BUTTON)
    browser.find_element(*SearchPage.MENU)
    browser.find_element(*SearchPage.TOP_SEARCH_BUTTON)
    browser.find_element(*SearchPage.TOP_SEARCH_FIELD)
