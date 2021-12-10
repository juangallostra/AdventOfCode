from helpers import parse_input

DAY = 3

def b2d(binary_str, exp=0):
    if len(binary_str) == 1:
        return 2 ** exp * int(binary_str)
    return 2 ** exp * int(binary_str[-1]) + b2d(binary_str[:-1], exp + 1)


def part1(data):
    gamma = ''.join(
            ['0' if sum([int(binary_num[bit_idx]) for binary_num in data]) < len(
                data)/2 else '1' for bit_idx in range(len(data[0]))]
    )
    map_data = {'1': '0', '0': '1'}
    epsilon = ''.join(map(lambda x: map_data[x], gamma))
    return b2d(epsilon) * b2d(gamma)


def part2(data):
    candidates_most = [d for d in data]
    candidates_least = [d for d in data]
    position = 0
    while len(candidates_most) > 1 or len(candidates_least) > 1:
        # diagnostic
        most_common = '0' if sum([int(binary_num[position]) for binary_num in candidates_most]) < len(
            candidates_most)/2 else '1'
        least_common = '1' if sum([int(binary_num[position]) for binary_num in candidates_least]) < len(
            candidates_least)/2 else '0'
        if len(candidates_most) > 1:
            candidates_most = [
                candidate for candidate in candidates_most if candidate[position] == most_common]
        if len(candidates_least) > 1:
            candidates_least = [
                candidate for candidate in candidates_least if candidate[position] == least_common]
        position += 1
    return b2d(candidates_most[0]) * b2d(candidates_least[0])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
