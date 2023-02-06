# LSP
# Пример нарушения LSP с помощью создания класса, который наследует Rectangle и не будет работать
# Dmitry: The use of properties here is deliberate, since we're redefining the 
# behavior of getters/setters in the derived class.

class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter     # прямое нарушение LSP
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter    # прямое нарушение LSP
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected area of {expected}, got {rc.area}')

# Whatever you have an interface taking some sort of base class, you should able to stick in any of its inheritors.
# Какой бы у вас ни был интерфейс, использующий какой-то базовый класс, вы должны иметь возможность использовать любого из его наследников.
sq = Square(5)
print(sq)
use_it(sq)
