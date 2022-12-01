from utils import parse_input

DAY = 7


def part1(data):
    data = [int(i) for i in data[0].split(',')]
    # sort data
    data = sorted(data)
    # get the median of the list
    median = data[len(data) // 2]
    return sum(abs(i - median) for i in data)


def cost(target, data):
    def abs_d(x): return abs(x-target)
    return sum(abs_d(x)*abs(x - target + (x-target)/abs_d(x))/2 if abs_d(x) > 1 else 1 for x in data)


def part2(data):
    data = sorted([int(i) for i in data[0].split(',')])
    mean = sum(data) / len(data)
    to_try = [round(mean-1), round(mean), round(mean+1)]
    vals = [cost(x, data) for x in to_try]
    return min(vals)


def old_part_2(data):
    data = sorted([int(i) for i in data[0].split(',')])
    # bruteforce the solution
    min_v = min(data)
    max_v = max(data)
    min_cost = -1
    for i in range(min_v, max_v+1):
        current_cost = cost(i, data)
        if min_cost == -1:
            min_cost = current_cost
        elif current_cost < min_cost:
            min_cost = current_cost
    return min_cost


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
