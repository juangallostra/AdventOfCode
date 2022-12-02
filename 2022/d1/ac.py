DAY = 1
YEAR = 2022


def parse_input(input_file):
    with open(input_file) as f:
        lines = []
        line = []
        for val in f.readlines():
            if val.strip():
                line.append(int(val))
            else:
                lines += [line]
                line = []
    return lines


def part1(m):
    return max(sum(vals) for vals in m)


def part2(m):
    return sum(sorted([sum(vals) for vals in m], reverse=True)[:3])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
