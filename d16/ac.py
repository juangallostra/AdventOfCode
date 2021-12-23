from utils import parse_input

DAY = 16

# utility functions
def hex_to_decimal(hex_str):
    return int(hex_str, 16)


def decimal_to_hex(x):
    return hex(x)[2:]


def decimal_to_binary(x):
    # return bin(decimal)[2:]
    bin = ''
    while x != 0:
        bin = str(x % 2) + bin
        x = x // 2
    return ('0000' + bin)[-4:]


def binary_to_decimal(bin_str):
    if len(bin_str) == 1:
        return int(bin_str)
    return 2**(len(bin_str)-1) * int(bin_str[0]) + binary_to_decimal(bin_str[1:])


class BITSParser():
    # This should only parse message lengths
    def __init__(self, message, should_convert=True):
        if should_convert:
            self._hex_message = message
            self._dec_message = [hex_to_decimal(i) for i in message]
            self._bin_message = ''.join([decimal_to_binary(a)
                                        for a in self._dec_message])
        else:
            self._bin_message = message
            self._hex_message = ''
            self._dec_message = ''

        self._message_to_process = self._bin_message

    @property
    def hexadecimal(self):
        return self._hex_message

    @property
    def decimal(self):
        return self._dec_message

    @property
    def binary(self):
        return self._bin_message

    @property
    def message_to_process(self):
        return self._message_to_process

    def get_next_packet(self):
        while self._message_to_process and '1' in self._message_to_process:
            yield self.get_packet()

    def get_packet_length(self, pointer=0):
        type_id = self._message_to_process[pointer+3:pointer+6]
        if binary_to_decimal(type_id) == 4:  # Literal packet
            end = False
            chunks = 0
            while not end:
                if self._message_to_process[pointer + 6 + (chunks * 5)] == '0':
                    end = True
                else:
                    chunks += 1
            return (6 + (chunks + 1) * 5)
        else:  # operator packet
            length_type_id = int(self._message_to_process[pointer + 6])
            if length_type_id == 0:
                data_length = binary_to_decimal(
                    self._message_to_process[pointer + 7:pointer + 7 + 15])
                return data_length + 7 + 15  # header + id + content + actual data
            elif length_type_id == 1:
                num_packets = binary_to_decimal(
                    self._message_to_process[pointer + 7:pointer + 7 + 11])
                # parse each packet
                length = 7 + 11
                # if only info i have is num packets I guess we'll have to parse the subpackets
                for _ in range(num_packets):
                    length += self.get_packet_length(pointer+length)
                return length

    def get_packet(self, pointer=0):
        length = self.get_packet_length(pointer)
        packet = self._message_to_process[pointer:pointer+length]
        self._message_to_process = self._message_to_process[pointer+length:]
        return packet


def get_packet_version(packet):
    return binary_to_decimal(packet[0:3])

def get_packet_type_id(packet):
    return binary_to_decimal(packet[3:6])

def try_get_subpackets(packet, pointer=0):
    type_id = packet[pointer+3:pointer+6]
    if binary_to_decimal(type_id) == 4:  # Literal packet, no subpackets
        return ''
    else:  # operator packet
        length_type_id = int(packet[pointer + 6])
        if length_type_id == 0:
            return packet[pointer + 7 + 15:]
        elif length_type_id == 1:
            return packet[pointer + 7 + 11:]


def decode_message(message):
    pass

def part1(data):
    to_parse = [data]
    is_hex = True
    versions = []
    while to_parse:
        parser = BITSParser(to_parse.pop(), should_convert=is_hex)
        is_hex = False
        for packet in parser.get_next_packet():  # get all packets at current main level
            # get version
            versions.append(get_packet_version(packet))
            subpackets = try_get_subpackets(packet)
            if subpackets:
                to_parse.append(subpackets)
    return sum(versions)


def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
