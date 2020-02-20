from selenium.webdriver.common.by import By


class AdminProductsPage:
    ADD_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')
    PRODUCT_ROW = (By.CSS_SELECTOR, 'tr')
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, 'td:nth-child(1) > input')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'td:nth-child(3)')
    PRODUCT_MODEL = (By.CSS_SELECTOR, 'td:nth-child(4)')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'td:nth-child(6)')
    PRODUCT_EDIT_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Edit"]')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div.alert-success')
