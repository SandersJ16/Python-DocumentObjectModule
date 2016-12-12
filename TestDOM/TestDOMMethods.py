import unittest
from DOM import XmlMaker


class TestXmlMakerMethods(unittest.TestCase):
    attribute_regex = r"(\s\w+=\".*\")"

    def test_renderSingleTag(self):
        tag_name = "table"

        xml = XmlMaker(tag_name)
        expected_xml = r"<{tag_name}></{tag_name}>".format(tag_name=tag_name)

        self.assertEqual(xml.__str__(), expected_xml);

    def test_renderTagWithSingleAttributes(self):
        tag_name = "element"
        attribute = "id"
        value = "test"

        xml = XmlMaker(tag_name).addAttribute(attribute, value)
        expected_xml = r'<{tag_name} {attribute}="{value}"></{tag_name}>'.format(tag_name=tag_name,
                                                                                 attribute=attribute,
                                                                                 value=value)

        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithMultipleAttributes(self):
        tag_name = "element"
        attributes = {"id"  : "test",
                      "name": "some_element"}

        xml = XmlMaker(tag_name)

        for attribute, value in attributes.items():
            xml.addAttribute(attribute, value)

        for attribute, value in attributes.items():
            expected_xml = r"<{tag_name}{attribute_regex}* {attribute}=\"{value}\"{attribute_regex}*></{tag_name}>".format(tag_name=tag_name,
                                                                                                                           attribute=attribute,
                                                                                                                           value=value,
                                                                                                                           attribute_regex=self.attribute_regex)
            self.assertRegex(xml.__str__(), expected_xml)

    def test_renderTagWithSingleAttributeAssignedMultipleTimes(self):
        tag_name = "form"
        attribute = "class"
        values = ["class_name", "default_class"]


        xml = XmlMaker(tag_name)
        for value in values:
            xml.addAttribute(attribute, value)

        for value in values:
            expected_xml = r'<{tag_name} {attribute}="(\w+ )?{value}( \w+)?"></{tag_name}>'.format(tag_name=tag_name,
                                                                                                   attribute=attribute,
                                                                                                   value=value)
            self.assertRegex(xml.__str__(), expected_xml)

    def test_overwritingAnAttribute(self):
        tag_name = "book"
        attribute = "genre"
        initial_value = "fantasy"
        overwrite_value = "sci-fi"

        xml = XmlMaker(tag_name).addAttribute(attribute, initial_value).setAttribute(attribute, overwrite_value)
        expected_xml = r'<{tag_name} {attribute}="{value}"></{tag_name}>'.format(tag_name=tag_name,
                                                                                 attribute=attribute,
                                                                                 value=overwrite_value)

        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithChildren(self):
        parent_tag = "table"
        child_tag = "tr"
        xml = XmlMaker(parent_tag).addChild(XmlMaker(child_tag))
        expected_xml = r"<{parent_tag}><{child_tag}></{child_tag}></{parent_tag}>".format(parent_tag=parent_tag,
                                                                                          child_tag=child_tag)
        self.assertEqual(xml.__str__(), expected_xml)

    def test_renderTagWithContent(self):
        tag_name = "speech"
        content = "I have a dream"

        xml = XmlMaker(tag_name).addContent(content)
        expected_xml = r"<{tag_name}>{content}</{tag_name}>".format(tag_name=tag_name,
                                                                    content=content)
        self.assertEqual(xml.__str__(), expected_xml)

    def test_manualSortOrders(self):
        parent_tag = "books"
        child_tag = "author"
        child_content = "Robert Heinlen"
        content_before_child = "hope"
        content_after_child = "test"


        xml = XmlMaker(parent_tag)
        xml.sort_order_iterator = 1000

        xml.addContent(content_after_child)

        xml.addChild(XmlMaker(child_tag).addContent(child_content), 500)
        xml.addContent(content_before_child, 250)
        expected_xml = r"<{parent_tag}>{first_content}<{child_tag}>{child_content}</{child_tag}>{second_content}</{parent_tag}>".format(parent_tag=parent_tag,
                                                                                                                                        child_tag=child_tag,
                                                                                                                                        child_content=child_content,
                                                                                                                                        first_content=content_before_child,
                                                                                                                                        second_content=content_after_child)
        self.assertEqual(xml.__str__(), expected_xml)

if __name__ == "__main__":
    unittest.main()
