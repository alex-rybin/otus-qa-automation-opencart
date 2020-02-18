from selenium.webdriver.common.by import By


class AdminBasePage:
    SIDE_MENU = (By.CSS_SELECTOR, '#menu')
    CATALOG_MENU_HEAD = (By.CSS_SELECTOR, 'a[href="#collapse1"]')
    PRODUCTS_MENU_ELEMENT = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2)')
