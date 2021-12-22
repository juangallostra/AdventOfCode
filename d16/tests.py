
import unittest
from d16.ac import BITSParser, try_get_subpackets, get_all_packet_versions
from utils import parse_input

DAY = 16

class AOCTests(unittest.TestCase):
    def test_single_literal_message(self):
        a = BITSParser('D2FE28')
        packet = a.get_next_packet()
        self.assertEqual(next(packet), '110100101111111000101')
        self.assertEqual(a.message_to_process, '000')

    def test_operator_packet(self):
        a = BITSParser('38006F45291200')
        self.assertEqual(a.binary, '00111000000000000110111101000101001010010001001000000000')
        l = a.get_packet_length()
        self.assertEqual(l, len('VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB'))

    def test_operator_packet_2(self):
        a = BITSParser('EE00D40C823060')
        self.assertEqual(a.binary, '11101110000000001101010000001100100000100011000001100000')
        l = a.get_packet_length()
        self.assertEqual(l, len('VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC'))
        pg = a.get_next_packet()
        np = next(pg)
        sp = try_get_subpackets(np)
        self.assertEqual(sp, '010100000011001000001000110000011')

    def test_add_versions_1(self):
        packet = '8A004A801A8002F478'
        versions = get_all_packet_versions(packet)
        self.assertListEqual(versions, [4,1,5,6])

    def test_add_versions_2(self):
        packet = '620080001611562C8802118E34'
        versions = get_all_packet_versions(packet)
        self.assertEqual(sum(versions), 12)

    def test_add_versions_3(self):
        packet = 'C0015000016115A2E0802F182340'
        versions = get_all_packet_versions(packet)
        self.assertEqual(sum(versions), 23)

    def test_add_versions_4(self):
        packet = 'A0016C880162017C3686B18A3D4780'
        versions = get_all_packet_versions(packet)
        self.assertEqual(sum(versions), 31)



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
