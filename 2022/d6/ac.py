
DAY = 6
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.rstrip('\n') for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def part1(data):
    stream = data[0]
    MARKER_LENGTH = 4
    for idx in range(len(stream)-MARKER_LENGTH):
        if len(set(stream[idx:idx+MARKER_LENGTH])) == MARKER_LENGTH:
            return idx + MARKER_LENGTH


def part2(data):
    stream = data[0]
    MARKER_LENGTH = 14
    for idx in range(len(stream)-MARKER_LENGTH):
        if len(set(stream[idx:idx+MARKER_LENGTH])) == MARKER_LENGTH:
            return idx + MARKER_LENGTH


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
