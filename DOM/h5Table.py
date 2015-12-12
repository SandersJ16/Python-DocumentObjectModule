from copy import deepcopy
from .xmlMaker import XmlMaker
from .orderedDictionary import OrderedDictionary


class H5Table(XmlMaker):
    def __init__(self, tag_id="", name=""):
        super().__init__("table")
        self._current_row = 0
        self._rows = OrderedDictionary()
        self._headers = []

        if tag_id:
            self.addAttribute("id", tag_id)
        if name:
            self.addAttribute("name", name)

        self._row_iterator = 1

    def addHeader(self, content):
        self._headers.append(content)

    def addRow(self):
        if len(self._rows) > 0:
            self._rows[self._rows.lastKey() + self._row_iterator] = []
        else:
            self._rows[self._row_iterator] = []

        self._current_row = self._rows.lastKey()
        return self

    def addCell(self, content="", colspan=1):
        cell = XmlMaker("td").addContent(content)
        if colspan > 1:
            cell.addAttribute("colspan", colspan)
        return self.addToCurrentRow(cell)

    def addToCurrentRow(self, child):
        self._rows[self._current_row].append(child)
        return self

    def changeRow(self, row_number):
        self._current_row = row_number
        return self

    def countRows(self):
        return len(self._rows)

    def countCellsInRow(self, row_number):
        return len(self._rows[row_number])

    def render(self):
        table = deepcopy(self)

        if len(table._headers) > 0:
            header_row = XmlMaker("tr")
            for header in table._headers:
                header_row.addChild(XmlMaker("th").addContent(header))
            table.addChild(header_row)

        if len(table._rows) > 0:
            for row, cells in sorted(table._rows.items()):
                current_row = XmlMaker("tr")
                for cell in cells:
                    current_row.addChild(cell)
                table.addChild(current_row)

        return super(H5Table, table).render()
