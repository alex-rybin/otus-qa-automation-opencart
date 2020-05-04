"""Тесты страницы Products"""
import allure
import mysql.connector as mariadb
import pytest
from envparse import env
from selenium.common.exceptions import ElementNotInteractableException

from pages.admin.add_product import AdminAddProduct
from pages.admin.base import AdminBasePage
from pages.admin.products import AdminProductsPage
from sql.commands import (
    clean_up,
    ADD_TEST_PRODUCT,
    ADD_TEST_PRODUCT_DESCRIPTION,
    GET_ID_BY_MODEL,
)


@pytest.fixture
def product_page(logged_admin_browser):
    """Переход на страницу Products"""
    page = AdminBasePage(logged_admin_browser)
    page.side_menu.click_menu_element('Catalog', 'Products')
    page = AdminProductsPage(logged_admin_browser)
    return page


@pytest.fixture
def add_test_product(request):
    """Добавляет тестовый продукт в БД и удаляет после прохождения теста"""
    db_connection = mariadb.connect(
        user=env.str('MARIADB_USER'),
        database=env.str('MARIADB_DATABASE'),
        host=env.str('MARIADB_HOST'),
    )
    cursor = db_connection.cursor()
    request.addfinalizer(lambda: clean_up(db_connection, cursor, 1))
    cursor.execute(ADD_TEST_PRODUCT)
    cursor.execute(ADD_TEST_PRODUCT_DESCRIPTION)
    db_connection.commit()


@pytest.fixture
def clear_added_product():
    """Удаляет продукт, созданный тестом"""
    yield
    db_connection = mariadb.connect(
        user=env.str('MARIADB_USER'),
        database=env.str('MARIADB_DATABASE'),
        host=env.str('MARIADB_HOST'),
    )
    cursor = db_connection.cursor()
    cursor.execute(GET_ID_BY_MODEL.format(model='cool test product'))
    product_id = int(cursor.fetchone()[0])
    clean_up(db_connection, cursor, product_id)


@allure.title('Фильтр по имени товара')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('keyword', ['ipod', 'iphone', 'samsung'])
def test_name_filter(product_page, keyword):
    try:
        product_page.filter_button.click()
    except ElementNotInteractableException:
        pass
    product_page.filter_form.filter_by('name', keyword)
    products = product_page.products_table.get_column_values('Product Name')
    assert all(keyword in product.lower() for product in products)
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Сортировка по количеству товаров')
@allure.severity(allure.severity_level.NORMAL)
def test_table_quantity_sorting(product_page):
    product_page.sort_table_by('Quantity')
    quantities = product_page.products_table.get_column_values('Quantity')
    assert quantities  # проверка на случай, если список вернётся пустым
    quantities = [int(quantity) for quantity in quantities]
    assert quantities == sorted(quantities, reverse=True)
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Сортировка по названию модели')
@allure.severity(allure.severity_level.NORMAL)
def test_table_model_sorting(product_page):
    product_page.sort_table_by('Model')
    models = product_page.products_table.get_column_values('Model')
    assert models  # проверка на случай, если список вернётся пустым
    assert models == sorted(models, reverse=True, key=str.casefold)
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Добавление нового продукта')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product(product_page, clear_added_product):
    test_product_name = 'test product 1'
    test_product_meta = 'autotest'
    test_product_model = 'cool test product'
    test_product_quantity = 100
    test_product_image = '/test_data/iphone8-test.png'
    product_page.click_add_product_button()
    add_product_page = AdminAddProduct(product_page.browser)
    add_product_page.edit_product_fields(
        test_product_name,
        test_product_meta,
        test_product_model,
        test_product_quantity,
        test_product_image,
    )
    product_page = AdminProductsPage(add_product_page.browser)
    products = product_page.products_table.get_table()
    added_product_found = False
    added_product_model = None
    added_product_quantity = None
    for product in products:
        name = product[2]
        if name == test_product_name:
            added_product_model = product[3]
            added_product_quantity = product[5]
            added_product_found = True
            break
    assert added_product_found
    assert added_product_model == test_product_model
    assert int(added_product_quantity) == test_product_quantity
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Удаление продукта')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_product(add_test_product, product_page):
    products = product_page.products_table.get_table()
    product_found = False
    row = None
    for product in enumerate(products):
        name = product[1][2]
        if name == '[test]product':
            row = product[0]
            product_found = True
            break
    assert product_found
    product_page.delete_products(row)
    product_deleted = True
    products = product_page.products_table.get_table()
    for product in products:
        name = product[2]
        if name == '[test]product':
            product_deleted = False
            break
    assert product_deleted
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'


@allure.title('Изменение продукта')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_product(add_test_product, product_page):
    test_product_name = 'test product 1'
    test_product_meta = 'autotest'
    test_product_model = 'cool test product'
    test_product_quantity = 1000
    products = product_page.products_table.get_table()
    test_product_found = False
    for product in enumerate(products):
        name = product[1][2]
        if name == '[test]product':
            product_page.start_product_edit(product[0])
            test_product_found = True
            edit_page = AdminAddProduct(product_page.browser)
            edit_page.edit_product_fields(
                test_product_name,
                test_product_meta,
                test_product_model,
                test_product_quantity,
            )
            break
    assert test_product_found

    products = product_page.products_table.get_table()
    edited_product_found = False
    edited_product_model = None
    edited_product_quantity = None
    for product in products:
        name = product[2]
        if name == test_product_name:
            edited_product_model = product[3]
            edited_product_quantity = product[5]
            edited_product_found = True
            break
    assert edited_product_found
    assert edited_product_model == test_product_model
    assert int(edited_product_quantity) == test_product_quantity
    logs = product_page.get_console_log()
    assert not logs, f'Errors from browser console: {logs}'
