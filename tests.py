import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_no_cols(self):
        num_cols = 0
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
    
    def test_maze_largish(self):
        num_cols = 10 ** 3
        num_rows = 10 ** 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,seed=5)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False,
        )
    
    def test_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.start_drawing()
        self.assertTrue(m1._cells[0][0].visited)
        self.assertTrue(m1._cells[4][4].visited)
    
    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.start_drawing()
        m1._reset_cells_visited()
        self.assertFalse(m1._cells[0][0].visited)
        self.assertFalse(m1._cells[4][4].visited)
    

if __name__ == "__main__":
    unittest.main()