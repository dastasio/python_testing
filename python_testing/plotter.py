from equation_solver import parse
import tkinter as tk

def solveForY(func = str, x = float):
    return parse(func, False, x)

class Plotter:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.entry = tk.Entry(master, width=100)
        self.entry.pack(side=tk.TOP)

        self.canvas = tk.Canvas(master, width=1024, height=720)
        self.canvas.pack()

        self.canvas.create_line(100, 0, 200, 360, width=1.0, fill='#b0b0b0')

    def init_grid(self, range)

root = tk.Tk()

app = Plotter(root)

root.mainloop()
try:
    root.destroy()
except tk.TclError:
    1 == 1