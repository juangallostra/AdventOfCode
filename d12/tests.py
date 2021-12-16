
import unittest
from d12.ac import  part1, part2
from utils import parse_input

DAY = 12

class AOCTests(unittest.TestCase):
    def test_part1(self):
        # Given
        inputs = parse_input(f'd{DAY}/data/test_input.txt')
        final_inp = []
        current_inp = []
        for a in inputs:
            if (a == ''):
                final_inp.append(current_inp)
                current_inp = []
            else:
                current_inp.append(a)
        expected_sols = parse_input(f'd{DAY}/data/test_sol_1.txt', to_int=True)
        # When
        for i in range(len(final_inp)):
            # Then
            self.assertEqual(part1(final_inp[i]), expected_sols[i])

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
