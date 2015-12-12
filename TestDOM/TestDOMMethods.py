import unittest
from DOM import XmlMaker


class TestXmlMakerMethods(unittest.TestCase):

    def test_renderSingleTag(self):
        xml = XmlMaker("table")
        expected_xml = "<table></table>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithSingleAttributes(self):
        xml = XmlMaker("element").addAttribute("id", "test")
        expected_xml = "<element id=\"test\"></element>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithMultipleAttributes(self):
        xml = XmlMaker("element").addAttribute("id", "test")
        xml.addAttribute("name", "some_element")
        expected_xml = "<element id=\"test\" name=\"some_element\"></element>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithSingleAttributeAssignedMultipleTimes(self):
        xml = XmlMaker("form").addAttribute("class", "class_name")
        xml.addAttribute("class", "default_class")
        expected_xml = "<form class=\"class_name default_class\"></form>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_overwritingAnAttribute(self):
        xml = XmlMaker("book").addAttribute("genre", "fantasy").addAttribute("genre", "drama")
        xml.setAttribute("genre", "sci-fi")
        expected_xml = "<book genre=\"sci-fi\"></book>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithChildren(self):
        xml = XmlMaker("table").addChild(XmlMaker("tr"))
        expected_xml = ("<table><tr></tr></table>")
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithContent(self):
        xml = XmlMaker("speech").addContent("I have a dream")
        expected_xml = "<speech>I have a dream</speech>"
        self.assertEqual(xml.__str__(), expected_xml)

    def test_manualSortOrders(self):
        xml = XmlMaker("books")
        xml.sort_order_iterator = 1000
        xml.addContent("test")
        xml.addChild(XmlMaker("author").addContent("Robert Hindland"), 500)
        xml.addContent("hope", 250)
        expected_xml = "<books>hope<author>Robert Hindland</author>test</books>"
        self.assertEqual(xml.__str__(), expected_xml)

if __name__ == "__main__":
    unittest.main()
