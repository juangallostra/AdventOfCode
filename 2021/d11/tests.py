
import unittest
from d11.ac import part1, part2, update_octopus, flash_octopus, update_after_flash
from utils import parse_input, pad_data, unpad_data

DAY = 11


class AOCTests(unittest.TestCase):
    def test_pad_data(self):
        # Given
        data = [[0, 2],
                [9, 1]]
                
        output = [[0,0,0,0], [0, 0, 2, 0],
                  [0, 9, 1, 0], [0,0,0,0]]
        # When
        result = pad_data(data)
        # Then
        self.assertListEqual(result, output)

    def test_unpad_data(self):
        # Given                
        data = [[0,0,0,0], [0, 0, 2, 0],
                  [0, 9, 1, 0], [0,0,0,0]]
        
        output = [[0, 2],
                [9, 1]]
        # When
        result = unpad_data(data)
        # Then
        self.assertListEqual(result, output)
        
    def test_increase_energy(self):
        # Given
        data = [[0, 2],
                [9, 1]]
        output = [[1, 3],
                  [10, 2]]
        # When
        result = update_octopus(data)
        # Then
        self.assertListEqual(result, output)

    def test_flash_octoupus(self):
        # Given
        data = [[0, 2],
                [10, 1]]
        output = [[0, 2],
                  [0, 1]]
        # When
        result = flash_octopus(data)
        # Then
        self.assertListEqual(result, output)

    def test_update_after_flash(self):
        # Given
        data_1 = [[0, 2],
                [7, 1]]
        output_1 = [[0, 3],
                  [8, 2]]
        data_2 = [[0, 2],
                  [7, 0]]
        output_2 = [[0, 4],
                    [9, 0]]

        # When
        result = update_after_flash(data_1)
        result_2 = update_after_flash(data_2)
        # Then
        self.assertListEqual(result, output_1)
        self.assertListEqual(result_2, output_2)

    def test_part1(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(
            f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
        # When
        result = part1(input)
        # Then
        self.assertEqual(expected_sol, result)

    # def test_part2(self):
    #     # Given
    #     input = parse_input(f'd{DAY}/data/test_input.txt')
    #     expected_sol = parse_input(
    #         f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
    #     # When
    #     result = part2(input)
    #     # Then
    #     self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
