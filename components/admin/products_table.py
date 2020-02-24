from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from components.base import BaseComponent


class ProductsTable(BaseComponent):
    """Таблица продуктов на странице Products в панели администратора"""

    HEAD = (By.CSS_SELECTOR, 'thead > tr')
    BODY = (By.CSS_SELECTOR, 'tbody')
    ROW = (By.CSS_SELECTOR, 'tr')
    CELL = (By.CSS_SELECTOR, 'td')
    CHILD = (By.CSS_SELECTOR, ':nth-child(1)')

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

    def get_column_values(self, column_name: str) -> List[str]:
        """Возвращает все значения по имени столбца"""
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

    def get_table(self) -> List[list]:
        """Возвращает таблицу в виде списка из списков, каждый из которых содержит элементы ряда"""
        values = []
        rows = self.body.find_elements(*self.ROW)
        for row in rows:
            cells = row.find_elements(*self.CELL)
            values.append([cell.text for cell in cells])
        return values

    def sort_by(self, column_name: str):
        """Кликает по заголовку столбца для сортировки таблицы"""
        head_cells = self.head.find_elements(*self.CELL)
        for head_cell in head_cells:
            if head_cell.text == column_name:
                head_cell.click()
                return
        raise ValueError(f'Couldn\'t find column with name "{column_name}"')

    def get_cell(self, column: Union[int, str], row: int) -> webelement:
        """Возвращает указанную ячейку таблицы. Столбец можно указать числом или названием"""
        if isinstance(column, str):
            head_cells = self.head.find_elements(*self.CELL)
            head_found = False
            for head_cell in head_cells:
                if head_cell.text == column:
                    head_cell.click()
                    head_found = True
                    column = head_cells.index(head_cell)
                    break
            if head_found:
                raise ValueError(f'Couldn\'t find column with name "{column}"')
        rows = self.body.find_elements(*self.ROW)
        return rows[row].find_elements(*self.CELL)[column]

    def click_cell_content(self, column: Union[int, str], row: int):
        """Делает клик по элементу внутри указанной ячейки таблицы. Столбец можно указать числом или названием"""
        cell = self.get_cell(column, row)
        cell.find_element(*self.CHILD).click()
