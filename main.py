import tkinter
from window import Window
from lines import Point, Line, Cell

def main():
    window = Window(800, 600)
    
    cell1 = Cell(window)
    cell2 = Cell(window)

    cell1.draw(100, 100, 200, 200)
    cell2.draw(300, 300, 400, 400)

    cell1.draw_move(cell2)
    cell1.draw_move(cell2, undo=True)
    
    
    window.wait_for_close()

if __name__ == "__main__":
    main()