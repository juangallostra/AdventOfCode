from typing import List, Union


DAY = 10
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False) -> Union[List[int], List[str]]:
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def part1(data):
    next_check = 20
    CHECK_STEP = 40
    x_reg = 1
    current_cycle_idx = 1
    overall_val = 0
    for instruction in data:
        # we have to options
        if 'noop' in instruction:
            if current_cycle_idx == next_check:
                overall_val += next_check * x_reg
                next_check += CHECK_STEP
            current_cycle_idx += 1  # and do nothing
        else:
            if current_cycle_idx == next_check:
                overall_val += next_check * x_reg
                next_check += CHECK_STEP
            current_cycle_idx += 1
            if current_cycle_idx == next_check:
                overall_val += next_check * x_reg
                next_check += CHECK_STEP
            current_cycle_idx += 1
            x_reg += int(instruction.lstrip('addx '))
    return overall_val


def should_draw(sprite_center, cycle):
    # transpose cycle val to 0-39
    # print(cycle // 40, cycle % 40)
    return sprite_center - 1 <= cycle % 40 <= sprite_center + 1


def part2(data):
    print(data)
    TOTAL_PIXELS = 240
    SCREEN_WIDTH = 40
    screen = TOTAL_PIXELS * '.'
    sprite_center_pos = 1
    current_cycle_idx = 0
    for instruction in data:
        # we have 3 options
        if current_cycle_idx >= TOTAL_PIXELS:
            break
        elif 'noop' in instruction:
            if should_draw(sprite_center_pos, current_cycle_idx):
                screen = screen[:current_cycle_idx] + \
                    '#' + screen[current_cycle_idx+1:]
            current_cycle_idx += 1
        else:
            if should_draw(sprite_center_pos, current_cycle_idx):
                screen = screen[:current_cycle_idx] + \
                    '#' + screen[current_cycle_idx+1:]
            current_cycle_idx += 1
            if should_draw(sprite_center_pos, current_cycle_idx):
                screen = screen[:current_cycle_idx] + \
                    '#' + screen[current_cycle_idx+1:]
            current_cycle_idx += 1
            sprite_center_pos += int(instruction.lstrip('addx '))
    return ('\n').join([screen[i:i+SCREEN_WIDTH] for i in range(0, TOTAL_PIXELS, SCREEN_WIDTH)])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2:\n{part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
