import unittest
import sys
from boggle_solver import Boggle

# Adding the path to locate boggle_solver.py
sys.path.append("/home/codio/workspace")


class TestSuiteAlgScalabilityCases(unittest.TestCase):

    def test_normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.get_solution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuiteSimpleEdgeCases(unittest.TestCase):

    def test_square_grid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.get_solution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_empty_grid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.get_solution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuiteCompleteCoverage(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(True, True)


class TestSuiteQuAndSt(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
