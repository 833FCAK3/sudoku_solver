import unittest
import functions

# I would like to add more tests in the future. Not really just wanna make a
# test commit.
class GridTestCase(unittest.TestCase):
    """Test for main()."""

    def test_main(self):
        """Does it work with a default grid?"""
        grid = [[6, 4, 0, 2, 0, 0, 3, 0, 0],
                [0, 0, 0, 9, 8, 0, 0, 0, 0],
                [0, 0, 7, 0, 1, 0, 0, 0, 0],
                [0, 0, 2, 3, 0, 0, 0, 0, 5],
                [0, 0, 4, 5, 6, 0, 0, 0, 0],
                [1, 0, 5, 0, 0, 9, 6, 7, 0],
                [0, 0, 6, 0, 0, 0, 5, 1, 7],
                [0, 0, 0, 0, 0, 0, 0, 3, 0],
                [7, 5, 3, 0, 0, 0, 0, 0, 4]]
        solved = functions.grid_solved(functions.main(grid))
        self.assertEqual(solved, True)


unittest.main()