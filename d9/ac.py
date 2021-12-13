from utils import parse_input

DAY = 9


def indices_to_check(x, y, max_x, max_y):
    return (
        (y, x-1 if x!=0 else max_x),
        (y-1 if y!=0 else max_y, x),
        (y, x+1),
        (y+1, x)
    )

def part1(data):
    data = [[int(num) for num in line] for line in data]
    total = 0
    for i in range(len(data)):  # rows
        for j in range(len(data[i])):  # columns
            # Get which indexes to check
            to_check = indices_to_check(j, i, len(data[i]), len(data))
            levels = []
            for corner in to_check:
                try:
                    levels.append(data[corner[0]][corner[1]])
                except IndexError:
                    pass
            if data[i][j] < min(levels):
                total += (data[i][j] + 1)
    return total


def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
