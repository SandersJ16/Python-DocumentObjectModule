from collections import OrderedDict


class XmlMaker(object):
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self._attributes = OrderedDict()
        self._children = {}
        self._content = {}
        self._greatest_sort_order = 0
        self._sort_order_iterator = 100

    def setAttribute(self, attribute, value):
        self._attributes[attribute] = [value]
        return self

    def addAttribute(self, attribute, value):
        if attribute in self._attributes:
            self._attributes[attribute].append(value)
        else:
            self.setAttribute(attribute, value)
        return self

    def addChild(self, child, _sort_order=None):
        if _sort_order is None:
            self._greatest_sort_order += self._sort_order_iterator
            self._children[self._greatest_sort_order] = child
        else:
            self._greatest_sort_order = max(_sort_order, self._greatest_sort_order)
            self._children[_sort_order] = child
        return self

    def addContent(self, content, _sort_order=None):
        if _sort_order is None:
            self._greatest_sort_order += self._sort_order_iterator
            self._content[self._greatest_sort_order] = content
        else:
            self._greatest_sort_order = max(_sort_order, self._greatest_sort_order)
            self._content[_sort_order] = content
        return self

    def render(self):
        xml = "<" + self.tag_name
        xml += self._renderAttributes(self._attributes)
        xml += ">"
        xml += self._renderChildrenAndContent()
        xml += "</" + self.tag_name + ">"

        return xml

    def _renderAttributes(self, attributes):
        xml = ""
        for attribute, values in attributes.items():
            xml += " " + attribute + "=\""
            for value in values:
                xml += value.__str__() + " "
            xml = xml[:-1] + "\""
        return xml

    def _renderChildren(self, children):
        xml = ""
        for child in children:
            xml += child.__str__()
        return xml

    def _renderChildrenAndContent(self):
        xml = ""
        content_and_children = dict(self._content)  # or orig.copy()
        content_and_children.update(self._children)
        sorted_content_and_children = OrderedDict(sorted(content_and_children.items()))

        for sort_order, xml_parts in sorted_content_and_children.items():
            xml += xml_parts.__str__()
        return xml

    def __str__(self):
        return self.render()

    @property
    def sort_order_iterator(self):
        return self._sort_order_iterator

    @sort_order_iterator.setter
    def sort_order_iterator(self, sort_order_iterator):
        self._sort_order_iterator = sort_order_iterator

    def countChildren(self):
        return len(self._children)
