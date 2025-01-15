from tkinter import Tk, BOTH, Canvas
from lines import Line

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.root.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)
        self.redraw()

    def wait_for_close(self):
        while self.root.running:
            self.redraw()

    def close(self):
        self.root.running = False
        self.root.destroy()
        
    
        
        
        



