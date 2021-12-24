
import unittest
from d17.ac import  part1, part2
from utils import parse_input

DAY = 17

class AOCTests(unittest.TestCase):
    def test_part1(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
        # When
        result = part1(input)
        # Then
        self.assertEqual(expected_sol, result)

    def test_part2(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
        # When
        result = part2(input)
        # Then
        self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
