class HtmlElement:
    ident_size = 2

    def __init__(self, name='', text='') -> None:
        self.name = name
        self.text = text
        self.elements = []
    
    def __str(self, ident):
        lines = []
        i = ' ' * (ident * self.ident_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((ident + 1) * self.ident_size)
            lines.append(f'{i1}{self.text}')
        
        for e in self.elements:
            lines.append(e.__str(ident + 1))
        
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)
    
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self) -> str:
        return str(self.__root)

builder = HtmlElement.create('ul')
# builder = HtmlBuilder('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
builder.add_child_fluent('li', 'hello')\
    .add_child_fluent('li', 'world')
print('Ordinary builder:')
print(builder)