class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    def __setattr__(self, name, value):
        if name in ("width", "height"):  # change both here.
            super().__setattr__("width", value)
            super().__setattr__("height", value)
        else:
            super().__setattr__(name, value)


def use_it(rc):
    rc.height = 10  
    w = rc.width
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
