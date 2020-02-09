from pages.main import MainPage


def test_elements(browser):
    """Проверка наличия основных элементов главной страницы"""
    browser.find_element(*MainPage.CART_BUTTON)
    browser.find_element(*MainPage.FEATURED)
    browser.find_element(*MainPage.MENU)
    browser.find_element(*MainPage.SEARCH_BUTTON)
    browser.find_element(*MainPage.SEARCH_FIELD)
