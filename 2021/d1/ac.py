DAY = 1

def parse_input(input_file):
    with open(input_file) as f:
        measurements = [int(l.strip()) for l in f.readlines()]
    return measurements


def part1(m):
    return sum([1 if m[i+1] > m[i] else 0 for i in range(len(m)-1)])


def part2(m):
    window_size=3
    return sum([1 if m[i+window_size] > m[i] else 0 for i in range(len(m)-window_size)])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
