from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):
    FEATURED = (By.CSS_SELECTOR, '#content > div.row')
