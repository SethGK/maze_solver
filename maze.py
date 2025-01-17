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
        self._reset_cells_visited()
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for col in range(self._num_cols): 
            col_cells = []
            for row in range(self._num_rows): 
                col_cells.append(Cell(self._win))  
            self._cells.append(col_cells)  
     
        for col in range(self._num_cols): 
            for row in range(self._num_rows):  
                self._draw_cells(col, row)
                 
    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    
    
    def _break_enter_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False

        self._draw_cells(0, 0)
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)



    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        while True:
            to_visit = []
            # left
            if col > 0 and not self._cells[col - 1][row].visited:
                to_visit.append((col - 1, row))
            # right
            if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
                to_visit.append((col + 1, row))
            # up
            if row > 0 and not self._cells[col][row - 1].visited:
                to_visit.append((col, row - 1))
            # down
            if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
                to_visit.append((col, row + 1))

            if len(to_visit) == 0:
                self._draw_cells(col, row)
                return

            direction = random.randrange(len(to_visit))
            move = to_visit[direction]

            if move[0] == col + 1:  # Moved right
                self._cells[col][row].has_right_wall = False
                self._cells[col + 1][row].has_left_wall = False
            elif move[0] == col - 1:  # Moved left
                self._cells[col][row].has_left_wall = False
                self._cells[col - 1][row].has_right_wall = False
            elif move[1] == row + 1:  # Moved down
                self._cells[col][row].has_bottom_wall = False
                self._cells[col][row + 1].has_top_wall = False
            elif move[1] == row - 1:  # Moved up
                self._cells[col][row].has_top_wall = False
                self._cells[col][row - 1].has_bottom_wall = False

            self._break_walls_r(move[0], move[1])

    def _reset_cells_visited(self):
        for col_cells in self._cells:
            for cell in col_cells:
                cell.visited = False

    def _solve_r(self, col, row):
        self._animate()
        self._cells[col][row].visited = True

        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True

        if (
            col > 0
            and not self._cells[col][row].has_left_wall
            and not self._cells[col - 1][row].visited
        ):
            self._cells[col][row].draw_move(self._cells[col - 1][row])
            if self._solve_r(col - 1, row):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col - 1][row], True)

        if (
            col < self._num_cols - 1
            and not self._cells[col][row].has_right_wall
            and not self._cells[col + 1][row].visited
        ):
            self._cells[col][row].draw_move(self._cells[col + 1][row])
            if self._solve_r(col + 1, row):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col + 1][row], True)

        if (
            row > 0
            and not self._cells[col][row].has_top_wall
            and not self._cells[col][row - 1].visited
        ):
            self._cells[col][row].draw_move(self._cells[col][row - 1])
            if self._solve_r(col, row - 1):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row - 1], True)

        if (
            row < self._num_rows - 1
            and not self._cells[col][row].has_bottom_wall
            and not self._cells[col][row + 1].visited
        ):
            self._cells[col][row].draw_move(self._cells[col][row + 1])
            if self._solve_r(col, row + 1):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row + 1], True)

        return False

    def _solve(self):
        return self._solve_r(0, 0)
