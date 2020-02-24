from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.admin.products_filter import ProductsFilter
from components.admin.products_table import ProductsTable
from pages.admin.add_product import AdminAddProduct
from pages.admin.base import AdminBasePage


class AdminProductsPage(AdminBasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
    OPEN_FILTER_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Filter"]')
    PRODUCT_ROW = (By.CSS_SELECTOR, 'tr')
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, 'td:nth-child(1) > input')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'td:nth-child(3)')
    PRODUCT_MODEL = (By.CSS_SELECTOR, 'td:nth-child(4)')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'td:nth-child(6)')
    PRODUCT_EDIT_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Edit"]')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div.alert-success')
    FILTER_FORM = (By.CSS_SELECTOR, '#filter-product')
    PRODUCT_TABLE = (By.CSS_SELECTOR, '#form-product')

    _filter_form = None
    _products_table = None

    @property
    def filter_button(self) -> webelement:
        return self.browser.find_element(*self.OPEN_FILTER_BUTTON)

    @property
    def filter_form(self) -> ProductsFilter:
        return ProductsFilter(
            self.browser.find_element(*self.FILTER_FORM), self.browser
        )

    @property
    def products_table(self) -> ProductsTable:
        return ProductsTable(
            self.browser.find_element(*self.PRODUCT_TABLE), self.browser
        )

    def sort_table_by(self, column_name: str):
        """Вызывает сортировку таблицы и ждёт перезагрузку страницы"""
        self.products_table.sort_by(column_name)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.PRODUCT_TABLE)
        )

    def click_add_product_button(self):
        """Нажимает кнопку добавления продукта и ждёт появления формы ввода данных"""
        self.browser.find_element(*self.ADD_BUTTON).click()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(AdminAddProduct.NAME_INPUT)
        )

    def start_product_edit(self, row: int):
        """Выбирает указанный ряд и нажимает кнопку изменения продукта"""
        self.products_table.click_cell_content(7, row)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(AdminAddProduct.NAME_INPUT)
        )

    def delete_products(self, *rows: int):
        """Выбирает указанные строки в таблице и нажимает кнопку удаления"""
        for row in rows:
            self.products_table.click_cell_content(0, row)
        self.browser.find_element(*self.DELETE_BUTTON).click()
        Alert(self.browser).accept()
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(AdminProductsPage.ALERT_SUCCESS)
        )
