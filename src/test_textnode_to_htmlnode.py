import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("Hello", TextType.TEXT)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "Hello")

    def test_bold(self):
        node = TextNode("Hello", TextType.BOLD)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Hello")

    def test_italic(self):
        node = TextNode("Hello", TextType.ITALIC)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "i")

    def test_code(self):
        node = TextNode("print()", TextType.CODE)
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "code")

    def test_link(self):
        node = TextNode(
            "Google",
            TextType.LINK,
            "https://google.com",
        )

        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Google")
        self.assertEqual(
            html.props,
            {"href": "https://google.com"},
        )

    def test_image(self):
        node = TextNode(
            "logo",
            TextType.IMAGE,
            "logo.png",
        )

        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(
            html.props,
            {
                "src": "logo.png",
                "alt": "logo",
            },
        )

    def test_invalid_type(self):
        node = TextNode("Hello", "INVALID")

        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()