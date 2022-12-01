from utils import parse_input
from utils import data_as_matrix_str


DAY = 13


def split_input(data):
    dots = []
    folds = []
    for line in data:
        if line == '':
            continue
        elif 'fold along' in line:
            parsed = line.replace('fold along ', '').split('=')
            folds.append((parsed[0], int(parsed[-1])))
        else:
            parsed = line.split(',')
            dots.append((int(parsed[0]), int(parsed[1])))
    return dots, folds

# idea: folds along x-axis: directly on data
#       folds along y-axis: transposed data
# This makes using a list of tuples/list to represent the matrix easier


def build_matrix(dots):
    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)
    return [[0 if (x, y) not in dots else 1 for x in range(max_x+1)] for y in range(max_y+1)]


def transpose(matrix): return list(zip(*matrix))


GET_FOLD_MATRIX = {'y': lambda x: x, 'x': transpose}


def fold(matrix, index):
    # split data by axis
    data_1 = matrix[:index]
    # revert, which is how the "bottom" part ends up after folding
    data_2 = matrix[index+1:][::-1]
    # combine
    def fold_value(x, y): return round((x + y) / 2 + 0.1)
    return [tuple(fold_value(data_1[i][j], data_2[i][j]) for j in range(len(data_1[0]))) for i in range(len(data_1))]


def part1(data):
    dots, folds = split_input(data)
    matrix = build_matrix(dots)
    # first fold
    result = fold(GET_FOLD_MATRIX[folds[0][0]](matrix), folds[0][1])
    return sum(sum(row) for row in result)


def part2(data):
    # folding madness
    dots, folds = split_input(data)
    matrix = build_matrix(dots)
    for current_fold in folds:
        one_fold_closer = fold(
            GET_FOLD_MATRIX[current_fold[0]](matrix), current_fold[1])
        matrix = GET_FOLD_MATRIX[current_fold[0]](one_fold_closer)
    return matrix


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2:\n{data_as_matrix_str(part2(data))}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
