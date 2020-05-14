"""	Przygotować klasę Kształt - i klasę która pozwala na zmianę rozmiarów
- z tych dwóch klas odziedziczyć klasy: Kwadrat, koło,

  w tych klasach zaimplementowac zmianę rozmiarów, zastanowić
 się jakie byłyby najlepsze parametry takiej metody,
"""


class Sizeable:
    def __init__(self, size):
        self.size = size

    def change(self, new_size):
        self.size = new_size

    def get_area(self):
        raise Exception


class FigureShape:
    def __init__(self, name):
        self.name = name


class FigureSquare(FigureShape, Sizeable):
    def __init__(self, name, size):
        FigureShape.__init__(self, name)
        Sizeable.__init__(self, size)

    def get_area(self):
        return self.size ** 2


class FigureCircle(FigureShape, Sizeable):
    def __init__(self, name, size):
        FigureShape.__init__(self, name)
        Sizeable.__init__(self, size)

    def get_area(self):
        return 3.14 * self.size ** 2

class FigureRectangle(FigureShape, Sizeable):
    def __init__(self, name, size):
        FigureShape.__init__(self, name)
        Sizeable.__init__(self, size)

    def get_area(self):
        return self.sizes["a"] * self.sizes["b"]


def main():
    k1 = FigureSquare("kw1", 4)
    ko1 = FigureCircle("ko1", 4)
    pr1 = FigureRectangle("pr1", 4)
    print(k1.__dict__)
    print(ko1.__dict__)
    print(pr1.__dict__)
    print(k1.get_area())
    print(ko1.get_area())
    print(pr1.get_area())


if __name__ == '__main__':
    main()
