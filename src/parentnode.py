from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag should not be None")

        if self.children is None:
            raise ValueError("ParentNode children should not be None")

        html = f"<{self.tag}"

        if self.props is not None:
            html += self.props_to_html()

        html += ">"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
