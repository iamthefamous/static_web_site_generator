import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_single_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_multiple_children(self):
        child1 = LeafNode("b", "Hello")
        child2 = LeafNode("i", "World")

        parent = ParentNode("div", [child1, child2])

        self.assertEqual(
            parent.to_html(),
            "<div><b>Hello</b><i>World</i></div>"
        )

    def test_deeply_nested_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [
                                LeafNode("strong", "Nested")
                            ]
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><section><p><strong>Nested</strong></p></section></div>"
        )

    def test_parent_with_props(self):
        child = LeafNode("span", "text")
        parent = ParentNode(
            "div",
            [child],
            {"class": "container", "id": "main"}
        )

        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>text</span></div>'
        )

    def test_no_tag_raises_value_error(self):
        child = LeafNode("span", "child")
        parent = ParentNode(None, [child])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_no_children_raises_value_error(self):
        parent = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_empty_children_list(self):
        parent = ParentNode("div", [])

        self.assertEqual(
            parent.to_html(),
            "<div></div>"
        )


if __name__ == "__main__":
    unittest.main()