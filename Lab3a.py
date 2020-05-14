"""	Przygotować klasę Kształt - i klasę która pozwala na zmianę rozmiarów
- z tych dwóch klas odziedziczyć klasy: Kwadrat, koło,
  w tych klasach zaimplementowac zmianę rozmiarów, zastanowić
 się jakie byłyby najlepsze parametry takiej metody,
"""


class Shape:
    def __init__(self, name):
        self.name = name


class SizeAble:
    def __init__(self, sizes):
        self.sizes = sizes

    def grow(self, size):
        self.size += 1

    def get_area(self):
        raise Exception


class Square(Shape, SizeAble):
    def __init__(self, name, size):
        Shape.__init__(self, name)
        SizeAble.__init__(self, size)

    def get_area(self):
        return self.size ** 2


class Circle(Shape, SizeAble):
    def __init__(self, name, sizes):
        Shape.__init__(self, name)
        SizeAble.__init__(self, sizes)

    def get_area(self):
        return 3.14 * self.size ** 2


class Rectangle(Shape, SizeAble):
    def __init__(self, name, sizes):
        Shape.__init__(self, name)
        SizeAble.__init__(self, sizes)

    def get_area(self):
        return 3.14 * self.sizes[] * self.sizes[1]


def main():
    kw1 = Square("kw1", [4])
    ko1 = Circle("ko1", [4])
    pr1 = Rectangle("pr1", [4, 5])
    print(kw1.__dict__)
    print(ko1.__dict__)
    print(kw1.get_area())
    print(ko1.get_area())


if __name__ == '__main__':
    main()