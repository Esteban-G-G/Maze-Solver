import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_square_grid(self):
        m2 = Maze(0, 0, 5, 5, 20, 20)
        self.assertEqual(len(m2._Maze__cells), 5)
        self.assertEqual(len(m2._Maze__cells[0]), 5)

    def test_maze_single_cell(self):
        m3 = Maze(0, 0, 1, 1, 30, 30)
        self.assertEqual(len(m3._Maze__cells), 1)
        self.assertEqual(len(m3._Maze__cells[0]), 1)

    def test_maze_entrance_exit(self):
        m = Maze(0,0,5,5,10,10)
        entrance = m._Maze__cells[0][0]
        exit_cell = m._Maze__cells[4][4]

    def test_reset_cells_visited(self):
        m = Maze(0, 0, 3, 3, 10, 10)
        # Manually set all visited to True
        for col in m._Maze__cells:
            for cell in col:
                cell.visited = True

        m._Maze__reset_cells_visited()

        # Check all are now False
        for col in m._Maze__cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
