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


def parse_literal_packet(packet):
    end = False
    chunks = 0
    data = []
    while not end:
        # append chunk
        data.append(packet[6 + (chunks * 5):6 + (chunks * 5) + 5])
        if packet[6 + (chunks * 5)] == '0':
            end = True
        else:
            chunks += 1
    return binary_to_decimal(''.join(chunk[1:] for chunk in data))


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
            # get a tring of all subpackets
            subpackets = try_get_subpackets(packet)
            if subpackets:
                to_parse.append(subpackets)
    return sum(versions)


class Packet():
    def __init__(self, type_id, data, parent) -> None:
        self.type_id = type_id
        self.data = data
        self.parent = parent
        # self.children = []

    def __repr__(self) -> str:
        return f'Packet(type id: {self.type_id}, data: {self.data}, parent: {self.parent})'


def part2(data):
    # Process the actual message
    to_parse = [data]
    stack = []  # build a stack of (operation_id, packet_content)
    is_hex = True
    while to_parse:
        # print(f'To parse: {to_parse}')
        parser = BITSParser(to_parse.pop(), should_convert=is_hex)
        is_hex = False
        for packet in parser.get_next_packet():  # get all packets at current level
            packets = []
            # for each packet at this level:
            # get type id
            type_id = get_packet_type_id(packet)
            # print(type_id)
            # print(f'Parsing: {packet}')
            # get subpackets
            subpackets = try_get_subpackets(packet)
            if subpackets:
                # print(f'sub: {subpackets}')
                # nested operations, append to packets to parse
                to_parse.append(subpackets)
                packets.append(subpackets)
            else:
                # print(f'Literal: {packet}')
                # Literal packet -> process it
                val = parse_literal_packet(packet)
                packets.append(val)
            stack.append(Packet(type_id, packets, parser.binary))
    # we have our stack, sort it by parent size (the shorter the parent
    # the more nested the packet is) and look for relations
    stack = sorted(stack, key=lambda x: len(x.parent))
    for packet_child in stack:
        # replace data with children
        for packet_parent in stack:
            if type(packet_parent.data) != Packet and packet_child.parent in packet_parent.data:
                packet_parent.data.append(packet_child)
    parsed_message = stack[-1]
    # print(stack)
    # flatten message
    # print(parsed_message)
    return compute_value(parsed_message)


def compute_value(packet):
    if packet.type_id == 4:
        return packet.data[0]
    elif packet.type_id == 0:
        return sum(compute_value(packet) for packet in packet.data[1:])
    elif packet.type_id == 1:
        from functools import reduce
        return reduce(lambda x, y: x*y, (compute_value(packet) for packet in packet.data[1:]))
    elif packet.type_id == 2:
        return min(compute_value(packet) for packet in packet.data[1:])
    elif packet.type_id == 3:
        return max(compute_value(packet) for packet in packet.data[1:])
    elif packet.type_id == 5:
        return 1 if compute_value(packet.data[1]) > compute_value(packet.data[2]) else 0
    elif packet.type_id == 6:
        return 1 if compute_value(packet.data[1]) < compute_value(packet.data[2]) else 0
    elif packet.type_id == 7:
        return 1 if compute_value(packet.data[1]) == compute_value(packet.data[2]) else 0

def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data[0])}')
    print(f'Part2: {part2(data[0])}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
