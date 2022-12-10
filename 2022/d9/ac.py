from typing import List, Union


DAY = 9
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False) -> Union[List[int], List[str]]:
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


head_movement_map = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def move_head(head_pos, move):
    return (head_pos[0] + head_movement_map[move][0], head_pos[1] + head_movement_map[move][1])


def update_knot(head_pos, tail_pos):
    # diagonal movement
    if abs(head_pos[0] - tail_pos[0]) + abs(head_pos[1] - tail_pos[1]) >= 3:
        if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
            return (tail_pos[0]+1, tail_pos[1]+1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
            return (tail_pos[0]+1, tail_pos[1]-1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
            return (tail_pos[0]-1, tail_pos[1]+1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            return (tail_pos[0]-1, tail_pos[1]-1)
    # the head is ever two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough
    elif abs(head_pos[0] - tail_pos[0]) == 2:
        return (
            tail_pos[0] + (head_pos[0] - tail_pos[0]) //
            abs(head_pos[0] - tail_pos[0]),
            tail_pos[1]
        )
    elif abs(head_pos[1] - tail_pos[1]) == 2:
        return (
            tail_pos[0],
            tail_pos[1] + (head_pos[1] - tail_pos[1]) //
            abs(head_pos[1] - tail_pos[1])
        )
    return tail_pos


def part1(data):
    moves = [(d.split()[0], int(d.split()[1])) for d in data]
    # apply movement
    head_pos = (0, 0)
    tail_pos = (0, 0)
    visited = [tail_pos]
    for m in moves:
        for _ in range(m[1]):
            head_pos = move_head(head_pos, m[0])
            # update tail and update visited
            tail_pos = update_knot(head_pos, tail_pos)
            if tail_pos not in visited:
                visited.append(tail_pos)
    return len(visited)


def part2(data):
    ROPE_LENGTH = 10  # H, 1, 2, 3, ..., 9
    moves = [(d.split()[0], int(d.split()[1])) for d in data]
    positions = [(0, 0) for _ in range(ROPE_LENGTH)]
    visited = [positions[-1]]  # starting tail position
    for m in moves:  # process each row
        for _ in range(m[1]):  # m[1] times
            # update head in move direction
            head_pos = move_head(positions.pop(0), m[0])
            # set rest of positions as current positions
            current_knot_positions = [p for p in positions]
            positions = [head_pos]  # updated rope positions
            for idx, knot in enumerate(current_knot_positions):  # move all knots
                # update knots and update visited
                updated_knot_pos = update_knot(positions[idx], knot)
                positions.append(updated_knot_pos)
            if positions[-1] not in visited:
                visited.append(positions[-1])
    return len(visited)


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
