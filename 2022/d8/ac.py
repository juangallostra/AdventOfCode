from typing import List, Union


DAY = 8
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
    visible_list_coords = []
    # 4 passes
    # horizontal left to right and right to left
    for horizontal_line_idx, tree_line in enumerate(data):
        # check visibility in each horizontal direction
        for tree_idx, tree_height in enumerate(tree_line):
            if tree_idx == 0:
                visible = True
            else:
                visible = int(tree_height) > max(
                    [int(th) for th in [*tree_line[:tree_idx]]])

            if visible and (horizontal_line_idx, tree_idx) not in visible_list_coords:
                visible_list_coords.append((horizontal_line_idx, tree_idx))
        # the other way around
        for tree_idx, tree_height in enumerate(tree_line[::-1]):
            if tree_idx == 0:
                visible = True
            else:
                visible = int(tree_height) > max(
                    [int(th) for th in [*tree_line[::-1][:tree_idx]]])

            if visible and (horizontal_line_idx, len(tree_line)-1-tree_idx) not in visible_list_coords:
                visible_list_coords.append(
                    (horizontal_line_idx, len(tree_line)-1-tree_idx))
    # do the same for vertical lines. Now, this might require some tweaking to the data? - not really, just a different type of indexing
    for vertical_line_idx in range(len(data[0])):  # for each vertical line
        # get vetical line
        vertical_line = ''.join([line[vertical_line_idx] for line in data])
        # analize vertical line the same way we did with horizontal lines  - just take care of the indexing
        for tree_idx, tree_height in enumerate(vertical_line):
            if tree_idx == 0:
                visible = True
            else:
                visible = int(tree_height) > max(
                    [int(th) for th in [*vertical_line[:tree_idx]]])

            if visible and (tree_idx, vertical_line_idx) not in visible_list_coords:
                visible_list_coords.append((tree_idx, vertical_line_idx))
        # the other way around
        for tree_idx, tree_height in enumerate(vertical_line[::-1]):
            if tree_idx == 0:
                visible = True
            else:
                visible = int(tree_height) > max(
                    [int(th) for th in [*vertical_line[::-1][:tree_idx]]])

            if visible and (len(vertical_line)-1-tree_idx, vertical_line_idx) not in visible_list_coords:
                visible_list_coords.append(
                    (len(vertical_line)-1-tree_idx, vertical_line_idx))
    return len(visible_list_coords)


def part2(data):
    # for each tree get rows and compute
    max_score = 0
    for row, h_line in enumerate(data):
        for col, tree_height in enumerate(h_line):
            # get stacks
            l_stack = data[row][0:col][::-1]  # reverse
            r_stack = data[row][col+1:]
            t_stack = ''.join([r[col] for r in data[0:row]])[
                ::-1]  # does not include row | reverse
            b_stack = ''.join([r[col] for r in data[row+1:]])
            # get visible lengths:
            # if any stack is empty, visibility = 0
            if any(len(stack) == 0 for stack in [l_stack, r_stack, t_stack, b_stack]):
                v_score = 0
            else:
                l_v = 1
                r_v = 1
                t_v = 1
                b_v = 1
                for idx, tree in enumerate(l_stack):
                    if int(tree_height) > int(tree) and idx < len(l_stack)-1:
                        l_v += 1
                    else:
                        break
                for idx, tree in enumerate(r_stack):
                    if int(tree_height) > int(tree) and idx < len(r_stack)-1:
                        r_v += 1
                    else:
                        break
                for idx, tree in enumerate(t_stack):
                    if int(tree_height) > int(tree) and idx < len(t_stack)-1:
                        t_v += 1
                    else:
                        break
                for idx, tree in enumerate(b_stack):
                    if int(tree_height) > int(tree) and idx < len(b_stack)-1:
                        b_v += 1
                    else:
                        break
                v_score = l_v * r_v * t_v * b_v
            if v_score > max_score:
                max_score = v_score
    return max_score


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
