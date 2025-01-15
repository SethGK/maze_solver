import tkinter
from window import Window
from lines import Point, Line

def main():
    window = Window(800, 600)
    
    l = Line(Point(50, 50), Point(400, 400))
    window.draw_line(l, "black")
    
    window.wait_for_close()

if __name__ == "__main__":
    main()