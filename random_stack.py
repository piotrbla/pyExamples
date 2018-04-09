from random import randint
from random import seed


class element:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class stos:
    def __init__(self, first):
        self.length = 1
        self.porownania = 0
        self.przypisania = 4
        self.last = element(first)

    def add(self, data):
        new = element(data)
        self.przypisania += 2
        new.prev = self.last
        self.przypisania += 1
        self.prev = new
        self.przypisania += 1
        self.length += 1
        self.przypisania += 1

    def erase(self):
        self.last = self.last.prev
        self.przypisania += 1
        self.length -= 1
        self.przypisania += 1
        self.porownania += 1

    def check(self):
        return self.last

    def display(self):
        elems = []
        cur = self.last
        for i in range(self.length):
            elems.append(cur.data)
            cur = cur.prev
        elems.reverse()
        print(elems)

    def operations(self):
        print("Przypisania:", self.przypisania)
        print("Porownania:", self.porownania, "\n")

    def clear(self):
        self.przypisania = 0
        self.porownania = 0

    def append_in(self, index, data):
        new = stos(None)
        length = self.length
        self.przypisania += 1
        for i in range(length - index):
            new.add(self.check().data)
            self.erase()
        self.add(data)
        for i in range(length - index):
            self.add(new.check().data)
            new.erase()

    def check_in(self, index):
        new = stos(None)
        length = self.length
        for i in range(length - 1 - index):
            new.add(self.check().data)
            self.erase()
        cur = self.check()
        for i in range(length - 1 - index):
            self.add(new.check().data)
            new.erase()
        return cur

    def erase_in(self, index, data):
        new = stos(None)
        length = self.length
        self.przypisania += 1
        for i in range(length - 1 - index):
            new.add(self.check().data)
            self.erase()
        self.add(data)
        for i in range(length - 1 - index):
            self.add(new.check().data)
            new.erase()

    def append_in_row(self):
        for i in range(1, 25):
            self.add(randint(0, 100))
            print("Po kolei ")
            self.display()
            self.operations()

    def append_start_end(self):
        ktora_strona = 1
        self.przypisania += 1
        for i in range(25 - 1):
            self.porownania += 1
            if ktora_strona == 1:
                self.add(randint(0, 100))
                ktora_strona = 0
                self.przypisania += 1
            elif ktora_strona == 0:
                self.append_in(0, randint(0, 100))
                ktora_strona = 1
                self.przypisania += 1
            print("Poczatek/Koniec ")
            self.display()
            self.operations()

    def append_randomly(self):
        for i in range(24):
            where = randint(0, self.length)
            if where == self.length:
                self.add(randint(0, 100))
            else:
                self.erase_in(where, randint(0, 100))
            print("Losowo ")
            self.display()
            self.operations()


def wyszukaj():
    struktura = stos(randint(0, 100))
    struktura.append_in_row()
    struktura.display()
    struktura.clear()
    for i in range(25):
        print(i + 1, "element: ", struktura.check_in(i).data)
        stos.display()


def usuwanie():
    print("USUWANIE!")
    for i in range(25):
        seed(99)
        struktura = stos(randint(0, 100))
        struktura.append_in_row()
        struktura.display()
        struktura.clear()
        struktura.erase_in(i)
        print("Usuwanie ", i + 1, " elementu")
        stos.display()
        print("")


struktura = stos(randint(0, 100))

struktura.append_in_row()

# struktura.append_randomly()

# struktura.append_start_end()

# wyszukaj()

# usuwanie()
