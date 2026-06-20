class HTMLNode():
    def __init__(self, tag: str | None = None, 
                 value: str | None = None, 
                 children: list["HTMLNode"] | None = None,
                 props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}
    
    def to_html(self) -> str | None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        formatted_string = ""
        for key, val in self.props.items():
            formatted_string += f" {key}=\"{val}\""
        return formatted_string 

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag, self.value, self.children, self.props})"       