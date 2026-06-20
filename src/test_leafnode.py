import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_with_tag_no_props(self):
        node = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

    def test_leaf_without_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_with_props(self):
        node = LeafNode(
            "a",
            "Google",
            {"href": "https://google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com" target="_blank">Google</a>'
        )

    def test_leaf_empty_value_raises(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_none_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_single_char_value(self):
        node = LeafNode("span", "A")
        self.assertEqual(node.to_html(), "<span>A</span>")

    def test_leaf_props_empty_dict(self):
        node = LeafNode("p", "Hello", {})
        self.assertEqual(node.to_html(), "<p>Hello</p>")


if __name__ == "__main__":
    unittest.main()