
import unittest
from d4.ac import  part1, part2, Board
from utils import parse_input

DAY = 4

class AOCTests(unittest.TestCase):
    def test_part1(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        called = [int(i) for i in input[0].split(',')] # Called numbers
        boards = [Board(input[i+1:i+6]) for i in range(len(input)) if input[i] == '']
        expected_sol = parse_input(f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
        # When
        result = part1([called, boards])
        # Then
        self.assertEqual(expected_sol, result)

    def test_part2(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        called = [int(i) for i in input[0].split(',')] # Called numbers
        boards = [Board(input[i+1:i+6]) for i in range(len(input)) if input[i] == '']
        expected_sol = parse_input(f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
        # When
        result = part2([called, boards])
        # Then
        self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
