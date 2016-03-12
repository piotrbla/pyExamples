import tkinter as tk


class NewWindow:
    def __init__(self, master, count):
        window = tk.Toplevel(master)
        text_value = "zażółć gęślą jaźń #%s" % count
        label = tk.Label(window, text=text_value)
        label.pack(side="top", fill="both", padx=10, pady=10)
