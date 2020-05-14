from tkinter import *
o = Tk( )
b1 = Button(o, text="Zwykły przycisk");
b1.pack()
b2 = Button(o, text="Wyjątkowy przycisk")
b2.pack()
b2["borderwidth"] = 35
b2["highlightthickness"] = 5
b2["padx"] = 10
b2["pady"] = 15
b2["underline"] = 0
o.mainloop()