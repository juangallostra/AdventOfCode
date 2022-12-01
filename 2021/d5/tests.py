
import unittest
from d5.ac import part1, part2, get_lines
from utils import parse_input

DAY = 5


class AOCTests(unittest.TestCase):
    def test_part1(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(
            f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
        data = get_lines(input)
        # When
        result = part1(data)
        # Then
        self.assertEqual(expected_sol, result)

    def test_part2(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(
            f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
        data = get_lines(input)
        # When
        result = part2(data)
        # Then
        self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
