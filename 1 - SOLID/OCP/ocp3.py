# OCP
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# Расширяем функционал двумя классами:
# Specification - это класс, который определяет определённый item соответствует определённому критерию
# Filter - фильтруем items по определённым критерям

class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

# Пример использования фильтров

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree  = Product('Tree', Color.GREEN, Size.LARGE)
    house  = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Large products:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large blue items:')
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')
