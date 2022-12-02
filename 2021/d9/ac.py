from utils import parse_input

DAY = 9
YEAR = 2021


def indices_to_check(x, y, max_x, max_y):
    return (
        (y, x-1 if x != 0 else max_x),
        (y-1 if y != 0 else max_y, x),
        (y, x+1),
        (y+1, x)
    )


def find_basins(data):
    basins = []
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
                basins.append((i, j))
    return basins


class Map:
    def __init__(self, data):
        self.map = data


def ff(x, y, previous_value, data):
    try:
        if data.map[y][x] == 9 or data.map[y][x] <= previous_value or data.map[y][x] == -1:
            return
        else:
            prev_val = data.map[y][x]
            data.map[y][x] = -1
            ff(x-1 if x != 0 else len(data.map[0]), y, prev_val, data)
            ff(x+1, y, prev_val, data)
            ff(x, y-1 if y != 0 else len(data.map), prev_val, data)
            ff(x, y+1, prev_val, data)
            # print('\n'.join([''.join(str(a)) for a in data]))
            # print()
    except:
        return


def get_basin_size(data):
    return len([i for line in data for i in line if i == -1])


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
    data = [[int(num) for num in line] for line in data]
    basins = find_basins(data)
    max_basins = [0, 0, 0]
    for basin in basins:
        data_map = Map([[i for i in line] for line in data])
        ff(basin[1], basin[0], -1, data_map)
        basin_size = get_basin_size(data_map.map)
        if basin_size > max_basins[0]:
            max_basins = sorted([basin_size, max_basins[1], max_basins[2]])
    # first find basins
    return max_basins[0] * max_basins[1] * max_basins[2]


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
