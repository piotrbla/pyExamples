"""Przygotować klasę do przechowywania Komentarzy
(jeden obiekt - jeden komentarz napisany przez jednego użytkownika)
- użytkownicy o różnych możliwościach (istnieje inna metoda do sprawdzania uprawnień
- klasa bazowa użytkownik
- klasy pochodne: zwykły i administrator (ma możliwość edycji nie swoich komentarzy)).
"""
#
#
# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def check_rights(self):
#         return False
#
#
# class NormalUser(User):
#     pass
#
#
# class AdminUser(User):
#     def check_rights(self):
#         return True
#
#
# class Comment():
#     def __init__(self, value, user):
#         self.value = value
#         self.user = user
#
#
# def main():
#     user1 = User('Piotr')
#     k1 = Comment('Tutaj piszemy', user1)
#     print(k1.__dict__)
#
#
# if __name__ == '__main__':
#     main()

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


class Rook:
    def __init__(self, field):
        self.field = field

    def can_move(self):
        return True


def main():
    w1 = Rook("a1")
    print('True', w1.can_move("a2"))



if __name__ == '__main__':
    main()


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

# class Item:
#     pass
#
#
# class ValueItem(Item):
#     pass
#
#
# class TrashItem(Item):
#     pass
#
#
# class Room:
#     def __init__(self, item):
#         self.przedmiot = item
#
#     def get_description(self):
#         return str(self.item)
#
#
# class Map:
#     def __init__(self):
#         self.rooms = []
#
#     def load_level(self):
#         self.rooms.append(Room())
#
#
# def main():
#     r1 = Room("potion")
#     print(r1.get_description())
#
#
# if __name__ == '__main__':
#     main()
