
DAY = 5
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.rstrip('\n') for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def get_stacks_and_moves(data):
    # get stack section
    stack_lines = []
    moves = 0
    for idx, line in enumerate(data):
        if not line:
            moves = idx+1
            break
        stack_lines.append(line)
    # reverse stack lines -> bottom to top
    s_reversed = stack_lines[::-1]
    stacks = {idx: [] for idx in s_reversed.pop(0).split()}
    # begin adding crates to stacks
    for line in s_reversed:
        for stack in range(len(stacks)):
            if line[(stack*4):(stack*4)+3:1][1] != ' ':
                stacks[str(stack + 1)].append(line[(stack*4):(stack*4)+3:1][1])
    return stacks, data[moves:]


def get_move(line):
    # remove trailing move:
    w = line.split()
    return int(w[1]), w[3], w[5]


def part1(data):
    stacks, moves = get_stacks_and_moves(data)
    # while moves: pop move and update stack
    for move in moves:
        _moves, _from, _to = get_move(move)
        for _ in range(_moves):
            stacks[_to].append(stacks[_from].pop())
    return ''.join([v[-1] for _, v in stacks.items()])


def part2(data):
    stacks, moves = get_stacks_and_moves(data)
    # while moves: pop move and update stack
    for move in moves:
        _moves, _from, _to = get_move(move)
        # extract crates to move
        to_move = stacks[_from][len(stacks[_from])-_moves:]
        stacks[_from] = stacks[_from][:len(stacks[_from])-_moves]
        stacks[_to] += to_move
    return ''.join([v[-1] for _, v in stacks.items()])


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
