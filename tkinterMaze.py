from tkinter import *

HALF_SIZE = 35
MARGIN = 100

okno = Tk()
Label(okno, text='Labirynty').grid(row=0)
Label(okno, text='Rekurencja').grid(row=1)
Button(okno, text='Rozwiąż brute-force').grid(row=0, column=1, sticky=W)
Button(okno, text='Rozwiąż inaczej').grid(row=1, column=1, sticky=W)
ramka = Frame(okno)
rysunek = Canvas(ramka, bg='cornsilk', width=1024, height=768)
rysunek.pack(fill=X)
rysunek.create_text(190, 8, text='Piszę sobie po rysunku, Zażółć gęślą jaźń.', font=('arial', 8, 'bold'))
xVal= MARGIN
yVal= MARGIN
even = True
for row in range(8, 0, -1):
    for line in "abcdefgh":
        print (line + str(row), end=' ')
        if even:
            fill = 'white smoke'
        else:
            fill = 'saddle brown'
        even = not even
        rysunek.create_line(xVal - HALF_SIZE, yVal - HALF_SIZE, xVal + HALF_SIZE, yVal + HALF_SIZE)
        # rysunek.create_rectangle(xVal - HALF_SIZE, yVal - HALF_SIZE, xVal + HALF_SIZE, yVal + HALF_SIZE, fill=fill)
        # rysunek.create_text(xVal, yVal, text=line + str(row), font=('arial', 8, 'bold'))
        xVal+=2*HALF_SIZE
    xVal = MARGIN
    yVal+=2*HALF_SIZE
    even = not even

ramka.grid(row=3, columnspan=2)
rysunek.configure()
okno.mainloop()
