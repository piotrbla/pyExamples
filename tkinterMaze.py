from tkinter import *

MARGIN = 20
ROOM_SIZE = 60
WALL_SIZE = ROOM_SIZE // 2 - 6
level_map = []


class Room:
    def __init__(self):
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.is_wall = False


def set_rooms_horizontal(room_w, room_e):
    room_w.east = room_e
    room_e.west = room_w


def set_rooms_vertical(room_n, room_s):
    room_n.south = room_s
    room_s.north = room_n


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


def write_number(drawing, x_val, y_val, i, fill):
    bigger_font = ('arial', 12, 'bold')

    x_with_wall_size = x_val + WALL_SIZE
    y_with_wall_size = y_val + WALL_SIZE
    room_size_without_wall = ROOM_SIZE - 2
    drawing.create_rectangle(x_val + 2, y_val + 2, x_val + room_size_without_wall
                             , y_val + room_size_without_wall, fill=fill, outline=fill)
    drawing.create_text(x_with_wall_size + 5, y_with_wall_size + 7, text=str(i), font=bigger_font)


def brute_force():
    from time import sleep
    fill_room = 'light grey'
    fill_wall = 'saddle brown'
    for j in range(10):
        i = 0
        x_val = MARGIN
        y_val = MARGIN
        for row in level_map:
            for room in row:
                if room.is_wall:
                    fill = fill_wall
                else:
                    fill = fill_room
                write_number(canvas, x_val, y_val, i+j, fill)
                x_val += ROOM_SIZE + 2
                i += 1
            x_val = MARGIN
            y_val += ROOM_SIZE + 1
        canvas.update_idletasks()
        sleep(0.1)

tk_window = Tk()
Label(tk_window, text='Labirynty').grid(row=0)
Label(tk_window, text='Rekurencja').grid(row=1)
Button(tk_window, text='Rozwiąż brute-force', command=brute_force).grid(row=0, column=1, sticky=W)
Button(tk_window, text='Rozwiąż inaczej').grid(row=1, column=1, sticky=W)
frame = Frame(tk_window)
canvas = Canvas(frame, bg='cornsilk', width=1648, height=1268)
canvas.pack(fill=X)
arial_font = ('arial', 8, 'bold')
# canvas.create_text(190, 8, text='Piszę sobie po rysunku, Zażółć gęślą jaźń.', font=arial_font)
rows = ["..#.................",
        "....#....#####......",
        "......##.........#..",
        ".......#........#...",
        "...#...#............",
        ".......#.......#....",
        ".......#......#.....",
        "....#...............",
        ".............#......",
        "............#.......",
        ".....#..............",
        ".......#............",
        "...........#........",
        "......#.............",
        "......#...#.........",
        "..............#.....",
        "................#..."]

rows_big = ["..#.................",
            "....#....#####......",
            "......##.........#..",
            ".......#........#...",
            "...#...#............",
            ".......#.......#....",
            ".......#......#.....",
            "....#...............",
            ".............#......",
            "............#.......",
            ".....#..............",
            ".......#............",
            "...........#........",
            "......#.............",
            "......#...#.........",
            "..............#.....",
            ".....#....#.........",
            "...............#....",
            ".........#..........",
            "................#..."]


def main():
    fill_room = 'light grey'
    fill_wall = 'saddle brown'
    for row in rows:
        level_row = []
        for c in row:
            room = Room()
            if c == '#':
                room.is_wall = True
            level_row.append(room)
        level_map.append(level_row)

    i = 0
    x_val = MARGIN
    y_val = MARGIN

    for row in level_map:
        for room in row:
            if room.is_wall:
                fill = fill_wall
            else:
                fill = fill_room
            canvas.create_rectangle(x_val, y_val, x_val + ROOM_SIZE, y_val + ROOM_SIZE, fill=fill, outline=fill)
            create_walls(canvas, x_val, y_val)
            x_val += ROOM_SIZE + 2
            i += 1
        x_val = MARGIN
        y_val += ROOM_SIZE + 1

    frame.grid(row=3, columnspan=2)
    canvas.configure()
    tk_window.mainloop()


if __name__ == '__main__':
    main()
