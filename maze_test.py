import unittest
from maze import Maze

class MockWindow:
    def __init__(self):
        self.lines_drawn = []

    def draw_line(self, line, fill_color="black"):
        self.lines_drawn.append((line, fill_color))

    def redraw(self):
        pass 

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.num_rows = 5
        self.num_cols = 5
        self.cell_size_x = 10
        self.cell_size_y = 10
        self.mock_win = MockWindow()
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.mock_win)
        self.maze._animate = lambda: None
        self.maze._draw_cells = lambda i, j: None

    def test_maze_create_cells(self):
        
        self.assertEqual(len(self.maze._cells), self.num_rows)  # Number of rows
        self.assertEqual(len(self.maze._cells[0]), self.num_cols)  # Number of columns
    
    def test_break_enter_and_exit(self):
    
        self.assertFalse(self.maze._cells[0][0].has_top_wall)
        self.assertFalse(self.maze._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall)

    def test_break_walls_r(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.maze._cells[i][j].visited = True

        self.maze._reset_cells_visited()

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.assertFalse(self.maze._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()
