import unittest
from d3.ac import part1, part2
from d3.ac import b2d
from utils import parse_input

DAY = 3

class AOCTests(unittest.TestCase):
    def test_binary_to_decimal(self):
        # Given
        data = ['10', '101', '011', '111', '000']
        # When
        result = [b2d(x) for x in data]
        # Then
        self.assertListEqual([2, 5, 3, 7, 0], result)
        
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
