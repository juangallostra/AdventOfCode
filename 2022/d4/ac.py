
DAY = 4
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def process_input(data):
    return [
        sorted(
            [
                tuple(int(id) for id in ids.split('-')) for ids in pair.split(',')
            ],
            key=lambda x: (x[0], -x[1])
        ) for pair in data
    ]


def part1(data):
    # fully contained
    return sum([1 if (pair[0][1] >= pair[1][1]) else 0 for pair in data])


def part2(data):
    # overlap
    return sum([1 if (pair[1][0] <= pair[0][1]) else 0 for pair in data])


def main(input_file):
    data = process_input(parse_input(input_file))
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
