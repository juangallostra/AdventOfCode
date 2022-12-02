from typing import List, Tuple
from utils import parse_input

DAY = 5
YEAR = 2021


def get_lines(data) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    lines = [l.split(' -> ') for l in data]
    vectors = [(point[0].split(','), point[1].split(',')) for point in lines]
    coords = [((int(vector[0][0]), int(vector[0][1])),
               (int(vector[1][0]), int(vector[1][1]))) for vector in vectors]
    return coords


def remove_diagonal_lines(data) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    lines = []
    for line in data:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            lines.append(line)
    return lines


def remove_diagonal_lines_non_45_degrees(data) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    lines = []
    for line in data:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            lines.append(line)
        if abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
            lines.append(line)
    return lines


def generate_line_set(segment: Tuple[Tuple[int, int], Tuple[int, int]]) -> set:
    full_segment = set()
    s_x0 = segment[0][0]
    s_x1 = segment[1][0]
    s_y0 = segment[0][1]
    s_y1 = segment[1][1]
    if s_x0 == s_x1:  # equal x, generate all y
        min_v = min(s_y0, s_y1)
        max_v = max(s_y0, s_y1)
        full_segment = set([(s_x0, y) for y in range(min_v, max_v+1)])
    elif s_y0 == s_y1:  # equal y, generate all x
        min_v = min(s_x0, s_x1)
        max_v = max(s_x0, s_x1)
        full_segment = set([(x, s_y0) for x in range(min_v, max_v+1)])
    else:  # diagonal
        dir_x = 1 if s_x0 < s_x1 else -1
        dir_y = 1 if s_y0 < s_y1 else -1
        full_segment = set([(s_x0 + i * dir_x, s_y0 + i * dir_y)
                           for i in range(0, abs(s_x0 - s_x1)+1)])
    return full_segment


def part1(data):
    candidates = remove_diagonal_lines(data)
    intersections = []
    for idx, line1 in enumerate(candidates):
        seg_1 = generate_line_set(line1)
        for line2 in candidates[idx+1:]:
            seg_2 = generate_line_set(line2)
            intersection = seg_1.intersection(seg_2)
            if len(intersection) > 0:
                intersections += list(intersection)
    return len(set(intersections))


def part2(data):
    candidates = remove_diagonal_lines_non_45_degrees(data)
    intersections = []
    for idx, line1 in enumerate(candidates):
        seg_1 = generate_line_set(line1)
        for line2 in candidates[idx+1:]:
            seg_2 = generate_line_set(line2)
            intersection = seg_1.intersection(seg_2)
            if len(intersection) > 0:
                intersections += list(intersection)
    return len(set(intersections))


def main(input_file):
    data = parse_input(input_file)
    data = get_lines(data)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
