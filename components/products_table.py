from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from components.base import BaseComponent


class ProductsTable(BaseComponent):
    HEAD = (By.CSS_SELECTOR, 'thead > tr')
    BODY = (By.CSS_SELECTOR, 'tbody')
    ROW = (By.CSS_SELECTOR, 'tr')
    CELL = (By.CSS_SELECTOR, 'td')

    _head = None
    _body = None

    @property
    def head(self) -> webelement:
        if not self._head:
            self._head = self.container.find_element(*self.HEAD)
        return self._head

    @property
    def body(self) -> webelement:
        if not self._body:
            self._body = self.container.find_element(*self.BODY)
        return self._body

    def get_rows_count(self) -> int:
        return len(self.body.find_elements(*self.ROW))

    def get_column_values(self, column_name: str):
        column_index = None
        head_cells = self.head.find_elements(*self.CELL)
        for head_cell in head_cells:
            if head_cell.text == column_name:
                column_index = head_cells.index(head_cell)
                break
        if not column_index:
            raise ValueError(f'Couldn\'t find column with name "{column_name}"')
        values = []
        for row in self.body.find_elements(*self.ROW):
            values.append(row.find_elements(*self.CELL)[column_index].text)
        return values

    def sort_by(self, column_name: str):
        head_cells = self.head.find_elements(*self.CELL)
        for head_cell in head_cells:
            if head_cell.text == column_name:
                head_cell.click()
                return
        raise ValueError(f'Couldn\'t find column with name "{column_name}"')
