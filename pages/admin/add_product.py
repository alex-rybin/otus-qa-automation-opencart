from selenium.webdriver.common.by import By

from pages.admin.base import AdminBasePage


class AdminAddProduct(AdminBasePage):
    """Страница добавления продукта"""
    NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    GENERAL_TAB = (By.CSS_SELECTOR, 'a[href="#tab-general"]')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    PRICE_INPUT = (By.CSS_SELECTOR, '#input-price')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')

    def edit_product_fields(self, name: str, meta_key: str, model: str, quantity: int = None):
        """Прописывает указанные значения в поля продукта и нажимает кнопку сохранения"""
        name_field = self.browser.find_element(*self.NAME_INPUT)
        name_field.clear()
        name_field.send_keys(name)
        meta_key_field = self.browser.find_element(*self.META_TAG_INPUT)
        meta_key_field.clear()
        meta_key_field.send_keys(meta_key)
        self.browser.find_element(*self.DATA_TAB).click()
        model_field = self.browser.find_element(*self.MODEL_INPUT)
        model_field.clear()
        model_field.send_keys(model)
        if quantity is not None:
            quantity_field = self.browser.find_element(*self.QUANTITY_INPUT)
            quantity_field.clear()
            quantity_field.send_keys(quantity)
        self.browser.find_element(*self.SAVE_BUTTON).click()
