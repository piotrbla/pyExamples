from random import randint
import tkinter as tk

MARGIN = 20


def create_walls(drawing, x, y):
    x_end = x + ROOM_SIZE
    y_end = y + ROOM_SIZE
    x_end_wall = x + WALL_SIZE
    y_end_wall = y + WALL_SIZE
    x_begin_wall = x_end - WALL_SIZE
    y_begin_wall = y_end - WALL_SIZE

    drawing.create_line(x, y, x_end_wall, y, fill='blue')
    drawing.create_line(x, y, x, y_end_wall, fill='blue')
    drawing.create_line(x_begin_wall, y, x_end, y, fill='blue')
    drawing.create_line(x_end, y, x_end, y_end_wall, fill='blue')
    drawing.create_line(x, y_end, x_end_wall, y_end, fill='blue')
    drawing.create_line(x, y_begin_wall, x, y_end, fill='blue')
    drawing.create_line(x_begin_wall, y_end, x_end, y_end, fill='blue')
    drawing.create_line(x_end, y_begin_wall, x_end, y_end, fill='blue')


def write_number(rysunek, x_val, y_val, i):
    bigger_font = ('arial', 18, 'bold')
    rysunek.create_text(x_val + WALL_SIZE, y_val + WALL_SIZE, text=str(i), font=bigger_font)


okno = tk.Tk()
large_font = ('Verdana',30)
entryVar = tk.StringVar(value='')
entry = tk.Entry(okno, textvariable=entryVar, font=large_font)
entry.focus_set()
entry.place(height=1001)
entry.grid(row=0, column=1, sticky=tk.W)
tk.Button(okno, text='Rozwiąż inaczej').grid(row=1, column=1, sticky=tk.W)
ramka = tk.Frame(okno)
rysunek = tk.Canvas(ramka, bg='cornsilk', width=1648, height=1268)
rysunek.pack(fill=tk.X)
arial_font = ('arial', 8, 'bold')
rysunek.create_text(190, 8, text='Piszę sobie po rysunku, Zażółć gęślą jaźń.', font=arial_font)
x_val = MARGIN
y_val = MARGIN

ROOM_SIZE = 100
WALL_SIZE = ROOM_SIZE // 2 - 6
fill_room = 'light grey'
fill_wall = 'saddle brown'
level_map = []
i = 0
# fill = fill_wall
fill = fill_room

m1 = randint(1, 10)
m2 = randint(1, 10)

for r in range(11):
    for c in range(11):
        if not ((r == m1 and c == m2) or (r == m2 and c == m1)):
            rysunek.create_rectangle(x_val, y_val, x_val + ROOM_SIZE, y_val + ROOM_SIZE, fill=fill, outline=fill)
        else:
            rysunek.create_rectangle(x_val, y_val, x_val + ROOM_SIZE, y_val + ROOM_SIZE, fill=fill_wall, outline=fill_wall)
        create_walls(rysunek, x_val, y_val)
        if r == 0:
            if c > 0:
                write_number(rysunek, x_val, y_val, c)
        elif c == 0:
            write_number(rysunek, x_val, y_val, r)
        else:
            if not ((r == m1 and c == m2) or (r == m2 and c == m1)):
                write_number(rysunek, x_val, y_val, r*c)
        # rysunek.create_text(xVal, yVal, text=line + str(row), font=('arial', 8, 'bold'))
        x_val += ROOM_SIZE + 2
        i += 1
    x_val = MARGIN
    y_val += ROOM_SIZE + 1

ramka.grid(row=3, columnspan=2)
rysunek.configure()

okno.mainloop()
