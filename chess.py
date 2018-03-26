class Field:
    def __init__(self, r, c):
        self.r = r
        self.c = chr(c + ord('A') - 1)


class Board:
    def __init__(self):
        self.fields = []
        for row in range(1, 9):
            row_fields = []
            for column in range(1, 9):
                row_fields.append(Field(row, column))
            self.fields.append(row_fields)

    def print(self):
        for rf in reversed(self.fields):
            for cf in rf:
                print(cf.c, end='')
                print(cf.r, end=' ')
            print()


b = Board()
b.print()

