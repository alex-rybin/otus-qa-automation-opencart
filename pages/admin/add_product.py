import logging
import os
from pathlib import Path

import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from js.commands import ADD_IMAGE_UPLOAD_FIELD
from pages.admin.base import AdminBasePage


class AdminAddProduct(AdminBasePage):
    """Страница добавления продукта"""

    NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    GENERAL_TAB = (By.CSS_SELECTOR, 'a[href="#tab-general"]')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    IMAGE_TAB = (By.CSS_SELECTOR, 'a[href="#tab-image"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    PRICE_INPUT = (By.CSS_SELECTOR, '#input-price')
    IMAGE_THUMBNAIL = (By.CSS_SELECTOR, '#thumb-image')
    EDIT_IMAGE_BUTTON = (By.CSS_SELECTOR, '#button-image')
    IMAGE_UPLOAD_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        '#filemanager button[data-dismiss="modal"]',
    )
    UPLOAD_FORM = (By.CSS_SELECTOR, '#form-upload > input')
    TEST_IMAGE = (By.CSS_SELECTOR, 'img[title="iphone8-test.p ng"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')

    def __init__(self, browser: webdriver):
        super().__init__(browser=browser)
        self.logger = logging.getLogger('AdminAddProduct')
        self.logger.info('Add product page initialized')

    def edit_product_fields(
        self,
        name: str,
        meta_key: str,
        model: str,
        quantity: int = None,
        image: str = None,
    ):
        """Прописывает указанные значения в поля продукта и нажимает кнопку сохранения"""
        self.logger.info('Start editing product fields')
        with allure.step('Изменение полей товара'):
            with allure.step(f'Ввод имени продукта: {name}'):
                name_field = self.browser.find_element(*self.NAME_INPUT)
                name_field.clear()
                name_field.send_keys(name)
            with allure.step(f'Ввод мета-ключа: {meta_key}'):
                meta_key_field = self.browser.find_element(*self.META_TAG_INPUT)
                meta_key_field.clear()
                meta_key_field.send_keys(meta_key)
            with allure.step('Переход на вкладку данных о товаре'):
                self.browser.find_element(*self.DATA_TAB).click()
            with allure.step(f'Ввод названия модели: {model}'):
                model_field = self.browser.find_element(*self.MODEL_INPUT)
                model_field.clear()
                model_field.send_keys(model)
            if quantity is not None:
                with allure.step(f'Ввод количества товара: {quantity}'):
                    quantity_field = self.browser.find_element(*self.QUANTITY_INPUT)
                    quantity_field.clear()
                    quantity_field.send_keys(quantity)
            if image:
                with allure.step(f'Отправка изображения: {image}'):
                    self.browser.find_element(*self.IMAGE_TAB).click()
                    self.browser.find_element(*self.IMAGE_THUMBNAIL).click()
                    self.browser.find_element(*self.EDIT_IMAGE_BUTTON).click()
                    close_button = WebDriverWait(self.browser, 1).until(
                        EC.visibility_of_element_located(self.IMAGE_UPLOAD_CLOSE_BUTTON)
                    )
                    self.browser.execute_script(
                        ADD_IMAGE_UPLOAD_FIELD.format(token=self.get_token())
                    )
                    close_button.click()
                    self.browser.find_element(*self.UPLOAD_FORM).send_keys(
                        os.path.join(Path(__file__).parent.parent.parent), image
                    )
                    WebDriverWait(self.browser, 10).until(EC.alert_is_present())
                with allure.step('Подтверждение загрузки изображения'):
                    Alert(self.browser).accept()
                with allure.step('Выбор нового превью'):
                    self.browser.find_element(*self.IMAGE_THUMBNAIL).click()
                    self.browser.find_element(*self.EDIT_IMAGE_BUTTON).click()
                    WebDriverWait(self.browser, 1).until(
                        EC.visibility_of_element_located(self.IMAGE_UPLOAD_CLOSE_BUTTON)
                    )
                    self.browser.find_element(*self.TEST_IMAGE).click()
            with allure.step('Сохранение изменений'):
                self.browser.find_element(*self.SAVE_BUTTON).click()
        self.logger.info('Product edited')
