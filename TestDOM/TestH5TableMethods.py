import unittest
from DOM import H5Table


class TestH5TableMethods(unittest.TestCase):

    def test_renderSimpleTable(self):
        table = H5Table("test")
        expected_xml = "<table id=\"test\"></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_addRow(self):
        table = H5Table()
        table.addRow()
        expected_xml = "<table><tr></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_addRowWithCells(self):
        table = H5Table()
        table.addRow()
        table.addCell("part 1")
        table.addCell("part 2")
        expected_xml = "<table><tr><td>part 1</td><td>part 2</td></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_addMultipleRowsWithCells(self):
        table = H5Table().addRow()
        table.addCell("books")
        table.addCell("are")
        table.addRow()
        table.addCell("the")
        table.addCell("best")
        expected_xml = "<table><tr><td>books</td><td>are</td></tr><tr><td>the</td><td>best</td></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_addCellThatSpansMultipleColumns(self):
        table = H5Table().addRow()
        table.addCell("", 3)
        expected_xml = "<table><tr><td colspan=\"3\"></td></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_changeToPreviousRow(self):
        table = H5Table().addRow()
        table.addRow()
        table.changeRow(1)
        table.addCell()
        expected_xml = "<table><tr><td></td></tr><tr></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_countRows(self):
        table = H5Table()
        self.assertEqual(table.countRows(), 0)
        table.addRow()
        self.assertEqual(table.countRows(), 1)
        table.addRow().addCell()
        self.assertEqual(table.countRows(), 2)

    def test_countChildrenInRow(self):
        table = H5Table()
        table.addRow()
        table.addRow().addCell()
        table.addRow().addCell().addCell()
        self.assertEqual(table.countCellsInRow(1), 0)
        self.assertEqual(table.countCellsInRow(2), 1)
        self.assertEqual(table.countCellsInRow(3), 2)

    def test_addHeader(self):
        table = H5Table()
        table.addHeader("H1")
        table.addRow().addCell("cell 1").addCell("cell 2")
        table.addHeader("H2")
        expected_xml = "<table><tr><th>H1</th><th>H2</th></tr><tr><td>cell 1</td><td>cell 2</td></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)

    def test_multipleRendersProduceSameOutput(self):
        table = H5Table("test_id")
        table.addHeader("H1")
        table.addRow().addCell("cell 1").addCell("cell 2")
        table.addRow().addCell("bat").addCell("man")
        table.addHeader("H2")
        expected_xml = "<table id=\"test_id\"><tr><th>H1</th><th>H2</th></tr><tr><td>cell 1</td><td>cell 2</td></tr><tr><td>bat</td><td>man</td></tr></table>"
        self.assertEqual(table.__str__(), expected_xml)
        self.assertEqual(table.__str__(), expected_xml)


if __name__ == "__main__":
    unittest.main()
