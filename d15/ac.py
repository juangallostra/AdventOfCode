from utils import parse_input, pad_data, unpad_data

DAY = 15

# pad with 10 so that we never move out of bounds

def part1(data):
    data = [[int(i) for i in row] for row in data]
    data = pad_data(data, 10)
    print(data)
    pass


def part2(data):
    data = [[int(i) for i in row] for row in data]
    print(data)
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
