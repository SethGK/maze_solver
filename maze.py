from lines import Point, Line, Cell
import time
import random

class Maze: 
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_enter_and_exit()
        self._break_walls_r(0, 0)
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                cell.draw(
                    self._x1 + j * self._cell_size_x,
                    self._y1 + i * self._cell_size_y,
                    self._x1 + (j + 1) * self._cell_size_x,
                    self._y1 + (i + 1) * self._cell_size_y,
                )
                row.append(cell)
            self._cells.append(row)

    def _draw_cells(self, i, j):
        cell = self._cells[i][j]
        cell.draw(
            self._x1 + j * self._cell_size_x,
            self._y1 + i * self._cell_size_y,
            self._x1 + (j + 1) * self._cell_size_x,
            self._y1 + (i + 1) * self._cell_size_y,
        )
        self._animate()

    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    
    
    def _break_enter_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cells(0, 0)
        self._draw_cells(self._num_rows - 1, self._num_cols - 1)

        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if not to_visit:
                self._draw_cells(i, j)
                return
            
            direction = random.randrange(len(to_visit))
            move = to_visit[direction]
            
            if move[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if move[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if move[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if move[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(move[0], move[1])
