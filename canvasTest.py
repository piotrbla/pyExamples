import tkinter as tk
from math import sqrt, cos, sin, radians

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.config(borderwidth=0.0, highlightthickness=0.0)


def create_sail(x_center, y_center, bigger_radius, smaller_radius, fill_color):
    points = []

    for theta in range(-90, 90, 1):
        alpha = radians(theta)
        x = x_center + bigger_radius * cos(alpha)
        y = y_center - 0.4 * bigger_radius * sin(alpha)
        points.extend([x, y])
    for theta in range(90, -90, -1):
        alpha = radians(theta)
        x = x_center + smaller_radius * cos(alpha)
        y = y_center - 0.9 * smaller_radius * sin(alpha)
        points.extend([x, y])
    canvas.create_polygon(points, fill=fill_color)

#
# from tkinter import *
#
# o = Tk()
# o.title("Let's Dream")
#
# o.geometry('800x530')
# c = Canvas(o, width=800, height=530, bg='MediumTurquoise')
#
# # szoty
# c.create_line(580, 240, 350, 420, width=1)
# c.create_line(600, 340, 490, 420, width=1)
# # c.create_line(580,370, 520,420, width = 1)
# c.create_line(550, 405, 530, 420, width=1)
#
# c.create_polygon(420, 110, 520, 40, 520, 220, 420, 110, width=1, fill='maroon')  # topsel F
# c.create_oval(200, -110, 535, 125, outline='MediumTurquoise', fill='MediumTurquoise')  # odcięcie topsel F
#
# c.create_polygon(420, 110, 520, 230, 520, 405, 345, 395, width=1, fill='maroon')  # Fok
# c.create_oval(250, -80, 425, 400, outline='MediumTurquoise', fill='MediumTurquoise', )  # odcięcie Fok
#
# c.create_polygon(220, 110, 332, 25, 333, 210, 223, 110, width=1, fill='maroon')  # topsel G
# c.create_oval(0, -110, 335, 125, outline='MediumTurquoise', fill='MediumTurquoise')  # odcięcie topsel G
#
# c.create_polygon(220, 115, 331, 215, 331, 405, 120, 395, 220, 115, width=1, fill='maroon')  # Grot
# c.create_oval(20, -80, 230, 400, outline='MediumTurquoise', fill='MediumTurquoise', )  # odcięcie Grot
#
# # fale z tyłu
# c.create_oval(0, 450, 335, 560, outline='DarkBlue', fill='DarkBlue')
# c.create_oval(-150, 440, 135, 530, outline='DarkBlue', fill='DarkBlue')
# c.create_oval(470, 460, 735, 530, outline='DarkBlue', fill='DarkBlue')
# c.create_oval(550, 450, 825, 550, outline='DarkBlue', fill='DarkBlue')
#
# c.create_polygon(130, 420, 650, 420, 570, 470, 220, 470, 130, 430, width=1, outline='black', fill='white')  # kadłub
# c.create_polygon(130, 430, 634, 430, 609, 445, 165, 445, width=1, fill='black')  # kadłub pasek
# # napis
# c.create_text((550, 446), text="Let's Dream", anchor=S, fill="white", font=("Arial", 10, 'italic'))
# c.grid(row=0)
#
# c.create_line(650, 420, 760, 395, width=5, fill='black')  # bukszpryt
# c.create_line(609, 445, 662, 438, width=1, fill='black')  # delfiniak1
# c.create_line(662, 438, 760, 395, width=1, fill='black')  # delfiniak2
# c.create_line(662, 438, 708, 406, width=1, fill='black')  # delfiniak3
# c.create_line(650, 420, 663, 438, width=2, fill='black')  # delfiniak4
#
# c.create_polygon(556, 98, 680, 290, 580, 240, width=1, outline='black', fill='maroon')  # latacz
# c.create_line(520, 42, 747, 395, width=1)
# c.create_polygon(536, 150, 747, 395, 600, 340, width=1, outline='black', fill='maroon')  # bomkliwer
# c.create_line(526, 138, 747, 395, width=1)  # forsztag
# # c.create_polygon(538,167,700,405,580,370,width = 1,outline = 'black', fill='maroon') #kliwer
# c.create_line(526, 152, 702, 406, width=1)  # sztag
# c.create_polygon(535, 183, 648, 415, 550, 405, width=1, outline='black', fill='maroon')  # sztafok
# c.create_line(528, 170, 650, 420, width=2)  # sztag
#
# c.create_line(220, 110, 333, 220, width=4, fill='black')  # gafel grotmaszt
# c.create_line(420, 110, 520, 230, width=4, fill='black')  # gafel fokmaszt
#
# c.create_polygon(120, 395, 332, 405, 332, 410, 120, 400, width=2, fill='black')  # bom grotmaszt
# c.create_line(125, 400, 150, 420, width=2)  # talia G
# c.create_polygon(345, 395, 522, 405, 522, 410, 345, 400, width=2, fill='black')  # bom fokmaszt
# c.create_line(350, 400, 375, 420, width=2)  # talia F
#
# c.create_polygon(330, 420, 260, 420, 260, 409, 290, 410, 330, 415, width=1, outline='black',
#                  fill='black')  # nadbudówka1
# c.create_polygon(520, 420, 460, 420, 460, 409, 470, 410, 520, 415, width=1, outline='black',
#                  fill='black')  # nadbudówka2
#
# c.create_line(338, 22, 520, 42, width=1)  # topsztag
#
# c.create_rectangle(520, 40, 526, 420, width=2, outline='black', fill='black')  # fokmaszt
# c.create_rectangle(332, 20, 338, 420, width=2, outline='black', fill='black')  # grotmaszt
#
# c.create_polygon(220, 115, 225, 120, 206, 145, 200, 140, width=1, outline='black', fill='white')  # bandera biały
# c.create_polygon(225, 120, 232, 124, 212, 150, 206, 145, width=1, outline='black', fill='maroon')  # bandera czerwony
#
# # fale 1 plan
# c.create_oval(-150, 440, 135, 500, outline='navy', fill='navy')
# c.create_oval(400, 450, 600, 600, outline='navy', fill='navy')
# c.create_oval(540, 470, 800, 600, outline='navy', fill='navy')
# c.create_oval(640, 450, 900, 600, outline='navy', fill='navy')
# c.create_oval(250, 460, 500, 610, outline='navy', fill='navy')
# c.create_oval(150, 450, 400, 590, outline='navy', fill='navy')
# c.create_oval(00, 460, 350, 590, outline='navy', fill='navy')
#
# o.mainloop()

create_sail(140, 180, 50, 20, 'royalblue')
create_sail(40, 80, 50, 20, 'royalblue')
canvas.pack()
root.mainloop()
