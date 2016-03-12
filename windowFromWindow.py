import tkinter as tk
from windowNewWindow import NewWindow

class View(tk.Frame):
    count = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        b = tk.Button(self, text="Otwórz nowe okno", command=self.new_window)
        b.pack(side="top")

    def new_window(self):
        self.count += 1
        NewWindow(self, self.count)


if __name__ == "__main__":
    root = tk.Tk()
    view = View(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
