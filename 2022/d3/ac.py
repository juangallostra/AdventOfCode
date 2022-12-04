
DAY = 3
YEAR = 2022


def get_priorities():
    return {
        chr(i): i-96 for i in range(97, 97+26)
    } | {chr(i): i-38 for i in range(65, 65+26)}


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def part1(data):
    prio = get_priorities()
    return sum([prio[(set(r[0:len(r)//2]) & set(r[len(r)//2:])).pop()] for r in data])


def part2(data):
    prio = get_priorities()
    # groups of 3
    idxs = [3*i for i in range(0, len(data)//3)]
    return sum([prio[(set(data[idx]) & set(data[idx+1]) & set(data[idx+2])).pop()] for idx in idxs])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
