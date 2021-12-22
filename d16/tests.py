
import unittest
from d16.ac import part1, part2, BITSParser
from utils import parse_input

DAY = 16


class AOCTests(unittest.TestCase):
    def test_single_literal_message(self):
        a = BITSParser('D2FE28')
        packet = a.get_next_packet()
        self.assertEqual(packet, '110100101111111000101000')

    def test_parser(self):
        a = BITSParser('D2FE28D2FE28')
        packet = a.get_next_packet()
        self.assertEqual(packet, '110100101111111000101000')
        self.assertEqual(a.message_to_process, '110100101111111000101000')

    def test_operator_packet(self):
        a = BITSParser('38006F45291200')
        self.assertEqual(a.binary, '00111000000000000110111101000101001010010001001000000000')

    def test_operator_packet_2(self):
        a = BITSParser('EE00D40C823060')
        self.assertEqual(a.binary, '11101110000000001101010000001100100000100011000001100000')

    # def test_part1(self):
    #     # Given
    #     input = parse_input(f'd{DAY}/data/test_input.txt')
    #     expected_sol = parse_input(
    #         f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
    #     # When
    #     result = part1(input)
    #     # Then
    #     self.assertEqual(expected_sol, result)

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
