import unittest
from maze import Maze

class MockWindow:
    def __init__(self):
        self.lines_drawn = []
        self.redraw_count = 0

    def draw_line(self, line, fill_color="black"):
        self.lines_drawn.append(line)

    def redraw(self):
        self.redraw_count += 1

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        mock_win = MockWindow()
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, mock_win)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_cell_drawing(self):
        num_cols = 12
        num_rows = 10
        mock_win = MockWindow()
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, mock_win)

        total_lines = num_cols * num_rows * 4
        self.assertEqual(len(mock_win.lines_drawn), total_lines)


if __name__ == "__main__":
    unittest.main()