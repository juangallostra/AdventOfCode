from utils import parse_input

DAY = 16

# utility functions


def hex_to_decimal(hex_str):
    return int(hex_str, 16)


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
    def __init__(self, message):
        self._hex_message = message
        self._dec_message = [hex_to_decimal(i) for i in message]
        self._bin_message = ''.join([decimal_to_binary(a)
                                    for a in self._dec_message])
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

    def get_packets(self):
        pass

    def get_packet_length(self, pointer=0):
        # TODO: replace _bin_message with _message_to_process
        type_id = self._bin_message[pointer+3:pointer+6]
        if binary_to_decimal(type_id) == 4: # Literal packet
            end = False
            chunks = 0
            while not end:
                if self._bin_message[pointer + 6 + (chunks * 5)] == '0':
                    end = True
                else:
                    chunks += 1
            return (6 + (chunks + 1) * 5) + 4 - (6 + (chunks + 1) * 5) % 4
        else: # operator packet
            length_type_id = int(self._bin_message[pointer + 6])
            if length_type_id == 0:
                data_length = binary_to_decimal(self._bin_message[pointer + 7:pointer + 7 + 15])
                return data_length + 7 + 15 # header + id + content + actual data
            elif length_type_id == 1:
                num_packets = binary_to_decimal(self._bin_message[pointer + 7:pointer + 7 + 11])
                # parse each packet
                length = 7 + 11
                for packet in range(num_packets): # if only info i have is num packets I guess we'll have to parse them
                    length += self.get_next_packet(pointer)

    def get_next_packet(self, pointer=0):
        length = self.get_packet_length(pointer)
        self._message_to_process = self._message_to_process[pointer+length:]
        return self._bin_message[pointer:pointer+length]


def part1(data):
    message_parser = BITSParser(data)

    pass


def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
