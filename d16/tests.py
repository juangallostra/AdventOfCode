
import unittest
from d16.ac import BITSParser, try_get_subpackets, part1, decode_message

DAY = 16

class AOCTests(unittest.TestCase):
    def test_packet_extraction(self):
        # Given
        a = BITSParser('D2FE28')
        # When
        packet = a.get_next_packet()
        # Then
        self.assertEqual(next(packet), '110100101111111000101')
        self.assertEqual(a.message_to_process, '000')

    def test_packet_length(self):
        # Given
        a = BITSParser('38006F45291200')
        # When
        l = a.get_packet_length()
        # Then
        self.assertEqual(a.binary, '00111000000000000110111101000101001010010001001000000000')
        self.assertEqual(l, len('VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB'))

    def test_packet_length_2(self):
        # Given
        a = BITSParser('EE00D40C823060')
        # When
        l = a.get_packet_length()
        # Then
        self.assertEqual(a.binary, '11101110000000001101010000001100100000100011000001100000')
        self.assertEqual(l, len('VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC'))

    def test_get_subpackets(self):
        # Given
        a = BITSParser('EE00D40C823060')
        # When
        pg = a.get_next_packet()
        np = next(pg)
        sp = try_get_subpackets(np)
        # Then
        self.assertEqual(sp, '010100000011001000001000110000011')

    def test_add_versions_1(self):
        # Given
        packet = '8A004A801A8002F478'
        # When
        result = part1(packet)
        # Then
        self.assertEqual(result, 16)

    def test_add_versions_2(self):
        # Given
        packet = '620080001611562C8802118E34'
        # When
        result = part1(packet)
        # Then
        self.assertEqual(result, 12)

    def test_add_versions_3(self):
        # Given
        packet = 'C0015000016115A2E0802F182340'
        # When
        result = part1(packet)
        # Then
        self.assertEqual(result, 23)

    def test_add_versions_4(self):
        # Given
        packet = 'A0016C880162017C3686B18A3D4780'
        # When
        result = part1(packet)
        # Then
        self.assertEqual(result, 31)

    # def test_parse_packet_1(self):
    #     # Given
    #     packet = 'C200B40A82'
    #     # When
    #     result = decode_message(packet)
    #     # Then
    #     self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
