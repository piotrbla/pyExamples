"""Zaimplementować klasę Mapa, która składa się z obiektów klasy Pokój
(pokój może być zamurowany - zmienna boolowska - wtedy do niego nie można wejść).
 W każdym niezamurowanym pokoju znajduje się obiekt klasy bazowej Przedmiot -
 ma ona 2 pochodne klasy: wartościowy, śmieć.
 Dorobić klasę gracz z listą przedmiotów,

  będziemy przesuwać gracza przy pomocy input
  (uwaga - w IDLE nie działa funkcja msvcrt.getch())
  i po wejściu do pokoju podnosi przedmiot.
  Po wpisaniu "wypisz" wypisywana jest lista przedmiotów.
  W wersji zaawansowanej mapę (z oznaczeniem przedmiotów) można wczytywać z pliku.
"""
#
#
# class Item:
#     pass
#
# class ValueableItem(Item):
#     pass
#
# class TrashItem(Item):
#     pass
#
#
# class Room:
#     def __init__(self, is_explorable):
#         self.is_explorable = is_explorable
#
# class Map:
#     def __init__(self):
#         self.rooms = []
#
#     def build_level(self):
#         if (True ): # z pliku
#             self.rooms.append(Room(True))
#         else:
#             self.rooms.append(Room(False))
"""Przygotować klasę do przechowywania Komentarzy
(jeden obiekt - jeden komentarz napisany przez jednego użytkownika)
- użytkownicy o różnych możliwościach (istnieje inna metoda do sprawdzania uprawnień
- klasa bazowa użytkownik
- klasy pochodne: zwykły i administrator (ma możliwość edycji nie swoich komentarzy)).
"""

#
# class Comment:
#     pass
#
#
# class User:
#     def has_rights(self):
#         return False
#
#
# class NormalUser(User):
#     def __init__(self, name):
#         self.name = name
#
#     def has_rights(self):
#         return super().has_rights()
#
#
# class AdminUser(User):
#     def has_rights(self):
#         return True
#
#
# def main():
#     u1 = NormalUser('Piotr')
#     k1 = Comment('To jest test', u1)
#
#
# if __name__ == '__main__':
#     main()
#


"""
Przygotować klasę bazową reprezentującą Figury szachowe 
- sprawdzenie prawidłowości wykonania ruchu na pustej szachownicy. 
Po klasie Figura (zgodnie z listą poniżej) dziedziczą klasy do weryfikacji 
poszczególnych rodzajów figur. W __init__ klasy bazowej podajemy pole startowe 
(numeracja pól od a1 do h8 - linie pionowe oznaczane literami od a do h, 
linie poziome liczbami od 1 do 8). 
Później dla obiektu są dwie metody: 
czy_mozna_ruch i wykonaj_ruch (to tylko propozycje nazwy), 
obydwie wywoływane z polem docelowym jako parametr. 
Druga z metod zmienia pole na którym znajduje się figura.
  Figura & reguła poruszania
  Pion do przodu o jedno pole,
      dwa pola w pierwszym ruchu 
  Wieża & Tylko w pionie i poziomie\\
  Skoczek & Dwa pola w pionie i jedno w poziomie \\
   & lub dwa pola w poziomie i jedno w pionie\\
  Goniec & Tylko po skosie \\
  Hetman & Po skosie, w pionie i poziomie \\
  Król & Po jednym polu po skosie, w pionie i poziomie\\
"""


#
# class Piece:
#     def __init__(self, field):
#         self.field = field
#
#     def can_move(self, target_field):
#         raise Exception
#
#
# class Rook(Piece):
#     def __init__(self, field):
#         super().__init__(field)
#
#     def can_move(self, target_field):
#         if self.field[0] == target_field[0] or self.field[1] == target_field[1]:
#             return True
#         else:
#             return False
#
#
# def main():
#     w1 = Rook('a1')
#     print('True', w1.can_move('a2'))
#     print('False', w1.can_move('b2'))

class Planet:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance


def save(planet):
    from datetime import datetime
    now = datetime.now()
    with open('planets.txt', 'at') as f:
        f.write(str(planet.name) + ';' + str(planet.distance) + ';' + now.strftime("%d/%m/%Y %H:%M:%S") + '\n')


def load_planets():
    planets = []
    with open('planets.txt', 'rt') as f:
        for line in f:
            values = line.split(';')
            x = Planet(values[0], values[1])
            planets.append(x)
    return planets

class Liczba:
    def __init__(self, v):
        self.value = int(v)
        if (self.value<0):
            raise ArithmeticError

    def show(self):
        print(self.value)


def odczyt_wartosc(plik):
    return -1

def main():
    x = 0
    while True:
        try:
            z = Liczba(input('Podaj wynik:'))
            break
        except:
            pass

    x = odczyt_wartosc('t.txt')
    try: #nie wolno tak robić
        s = Liczba(x)
    except ArithmeticError:
        pass

    z.show()
    p1 = Planet('Wenus', 3)
    p2 = Planet('Merkury', 4)
    for p in [p1, p2]:
        save(p)

    planets = load_planets()
    for p in planets:
        print(p.__dict__)


if __name__ == '__main__':
    main()
