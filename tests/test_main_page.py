import allure

from pages.store.main import MainPage


@allure.feature('Наличие элементов страницы')
@allure.title('Главная страница')
@allure.severity(allure.severity_level.CRITICAL)
def test_elements(browser):
    page = MainPage(browser)
    elements_visible = [
        page.cart_button.is_displayed(),
        page.featured.is_displayed(),
        page.menu.is_displayed(),
        page.top_search_button.is_displayed(),
        page.top_search_field.is_displayed(),
    ]
    expected = [True] * 5
    assert elements_visible == expected
    logs = page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
