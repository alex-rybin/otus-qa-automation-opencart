from time import sleep

import mysql.connector as mariadb
import pytest
from envparse import env
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import BASE_URL
from pages.admin.admin_add_product import AdminAddProduct
from pages.admin.admin_base import AdminBasePage
from pages.admin.admin_login import AdminLoginPage
from pages.admin.admin_products import AdminProductsPage
from sql.commands import (
    ADD_TEST_PRODUCT,
    clean_up,
    ADD_TEST_PRODUCT_DESCRIPTION,
    GET_ID_BY_MODEL,
)


@pytest.fixture
def logged_admin_browser(browser):
    """Открывает страницу входа администратора и логинится"""
    env.read_envfile()
    browser.get(BASE_URL + 'admin/')
    login_field = browser.find_element(*AdminLoginPage.USERNAME_FIELD)
    password_field = browser.find_element(*AdminLoginPage.PASSWORD_FIELD)
    login_button = browser.find_element(*AdminLoginPage.LOGIN_BUTTON)
    login_field.send_keys(env.str('OPENCART_LOGIN'))
    password_field.send_keys(env.str('OPENCART_PASSWORD'))
    login_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(AdminBasePage.SIDE_MENU)
    )
    return browser


@pytest.fixture
def add_test_product(request):
    """Добавляет тестовый продукт в БД и удаляет после прохождения теста"""
    db_connection = mariadb.connect(
        user=env.str('MARIADB_USER'),
        database=env.str('MARIADB_DATABASE'),
        host=env.str('MARIADB_IP'),
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
        host=env.str('MARIADB_IP'),
    )
    cursor = db_connection.cursor()
    cursor.execute(GET_ID_BY_MODEL.format(model='cool test product'))
    product_id = int(cursor.fetchone()[0])
    clean_up(db_connection, cursor, product_id)


def test_add_product(logged_admin_browser, clear_added_product):
    test_product_name = 'test product 1'
    test_product_meta = 'autotest'
    test_product_model = 'cool test product'
    test_product_quantity = '100'
    logged_admin_browser.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(logged_admin_browser, 1).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    add_button = WebDriverWait(logged_admin_browser, 5).until(
        EC.visibility_of_element_located(AdminProductsPage.ADD_BUTTON)
    )
    add_button.click()
    name_field = WebDriverWait(logged_admin_browser, 5).until(
        EC.visibility_of_element_located(AdminAddProduct.NAME_INPUT)
    )
    name_field.send_keys(test_product_name)
    logged_admin_browser.find_element(*AdminAddProduct.META_TAG_INPUT).send_keys(
        test_product_meta
    )
    logged_admin_browser.find_element(*AdminAddProduct.DATA_TAB).click()
    logged_admin_browser.find_element(*AdminAddProduct.MODEL_INPUT).send_keys(
        test_product_model
    )
    quantity_field = logged_admin_browser.find_element(*AdminAddProduct.QUANTITY_INPUT)
    quantity_field.clear()
    quantity_field.send_keys(test_product_quantity)
    logged_admin_browser.find_element(*AdminAddProduct.SAVE_BUTTON).click()
    WebDriverWait(logged_admin_browser, 5).until(
        EC.visibility_of_element_located(AdminProductsPage.ALERT_SUCCESS)
    )
    products = logged_admin_browser.find_elements(*AdminProductsPage.PRODUCT_ROW)
    added_product_found = False
    added_product_model = None
    added_product_quantity = None
    for product in products:
        name = product.find_element(*AdminProductsPage.PRODUCT_NAME).text
        if name == test_product_name:
            added_product_model = product.find_element(
                *AdminProductsPage.PRODUCT_MODEL
            ).text
            added_product_quantity = product.find_element(
                *AdminProductsPage.PRODUCT_QUANTITY
            ).text
            added_product_found = True
            break
    assert added_product_found
    assert added_product_model == test_product_model
    assert added_product_quantity == test_product_quantity


def test_delete_product(logged_admin_browser, add_test_product):
    logged_admin_browser.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(logged_admin_browser, 1).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    products = logged_admin_browser.find_elements(*AdminProductsPage.PRODUCT_ROW)
    product_found = False
    for product in products:
        name = product.find_element(*AdminProductsPage.PRODUCT_NAME).text
        if name == '[test]product':
            product.find_element(*AdminProductsPage.PRODUCT_CHECKBOX).click()
            product_found = True
            break
    assert product_found
    logged_admin_browser.find_element(*AdminProductsPage.DELETE_BUTTON).click()
    Alert(logged_admin_browser).accept()
    WebDriverWait(logged_admin_browser, 5).until(
        EC.visibility_of_element_located(AdminProductsPage.ALERT_SUCCESS)
    )
    product_deleted = True
    products = logged_admin_browser.find_elements(*AdminProductsPage.PRODUCT_ROW)
    for product in products:
        name = product.find_element(*AdminProductsPage.PRODUCT_NAME).text
        if name == '[test]product':
            product.find_element(*AdminProductsPage.PRODUCT_CHECKBOX).click()
            product_deleted = False
            break
    assert product_deleted


def test_edit_product(logged_admin_browser, add_test_product):
    test_product_name = 'test product 1'
    test_product_meta = 'autotest'
    test_product_model = 'cool test product'
    test_product_quantity = '1000'
    logged_admin_browser.find_element(*AdminBasePage.CATALOG_MENU_HEAD).click()
    products_menu_link = WebDriverWait(logged_admin_browser, 1).until(
        EC.visibility_of_element_located(AdminBasePage.PRODUCTS_MENU_ELEMENT)
    )
    products_menu_link.click()
    products = logged_admin_browser.find_elements(*AdminProductsPage.PRODUCT_ROW)
    test_product_found = False
    for product in products:
        name = product.find_element(*AdminProductsPage.PRODUCT_NAME).text
        if name == '[test]product':
            product.find_element(*AdminProductsPage.PRODUCT_EDIT_BUTTON).click()
            test_product_found = True
            name_field = WebDriverWait(logged_admin_browser, 5).until(
                EC.visibility_of_element_located(AdminAddProduct.NAME_INPUT)
            )
            name_field.clear()
            name_field.send_keys(test_product_name)
            meta_tag_field = logged_admin_browser.find_element(*AdminAddProduct.META_TAG_INPUT)
            meta_tag_field.clear()
            meta_tag_field.send_keys(test_product_meta)
            logged_admin_browser.find_element(*AdminAddProduct.DATA_TAB).click()
            model_field = logged_admin_browser.find_element(*AdminAddProduct.MODEL_INPUT)
            model_field.clear()
            model_field.send_keys(test_product_model)
            quantity_field = logged_admin_browser.find_element(*AdminAddProduct.QUANTITY_INPUT)
            quantity_field.clear()
            quantity_field.send_keys(test_product_quantity)
            logged_admin_browser.find_element(*AdminAddProduct.SAVE_BUTTON).click()
            WebDriverWait(logged_admin_browser, 5).until(
                EC.visibility_of_element_located(AdminProductsPage.ALERT_SUCCESS)
            )
            break
    assert test_product_found

    products = logged_admin_browser.find_elements(*AdminProductsPage.PRODUCT_ROW)
    edited_product_found = False
    edited_product_model = None
    edited_product_quantity = None
    for product in products:
        name = product.find_element(*AdminProductsPage.PRODUCT_NAME).text
        if name == test_product_name:
            edited_product_model = product.find_element(
                *AdminProductsPage.PRODUCT_MODEL
            ).text
            edited_product_quantity = product.find_element(
                *AdminProductsPage.PRODUCT_QUANTITY
            ).text
            edited_product_found = True
            break
    assert edited_product_found
    assert edited_product_model == test_product_model
    assert edited_product_quantity == test_product_quantity
