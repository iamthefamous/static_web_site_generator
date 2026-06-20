from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None,value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str | None:
        if self.value == None or len(self.value) == 0:
            raise ValueError("LeafNode must have a value")

        if self.tag == None:
            return self.value
        
        formatted_str = f"<{self.tag}"
        if self.tag is not None:
            formatted_str += self.props_to_html()
        formatted_str += '>'
        formatted_str += f"{self.value}</{self.tag}>"

        return formatted_str

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
