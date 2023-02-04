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

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    # Тут мы нарушаем OCP принцип. OCP принцип гласит, что при добавлении функционала, 
    # вы добавляете его через расширение, а не через исправление.
    # OCP = open for extension, closed for modification
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree  = Product('Tree', Color.GREEN, Size.LARGE)
    house  = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')