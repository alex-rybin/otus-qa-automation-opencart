from selenium.webdriver.common.by import By

from pages.admin.admin_base import AdminBasePage


class AdminAddProduct(AdminBasePage):
    NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    GENERAL_TAB = (By.CSS_SELECTOR, 'a[href="#tab-general"]')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    PRICE_INPUT = (By.CSS_SELECTOR, '#input-price')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')
