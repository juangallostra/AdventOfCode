from utils import parse_input, pad_data, unpad_data

DAY = 11

# Process:
# 1. Update energy levels
# 2. Flash octopus
# While there was a flash in the last iteration:
#   3. Update energy levels - skip already flashed and mark them as processed
#   4. Flash octopus
# 5. Count flashes
# 6. Repeat from 1

def update_octopus(data):
    return [[i+1 for i in row] for row in data]


def flash_octopus(data):
    return [[0 if i > 9 else i for i in row] for row in data]


def count_flashes(data):
    return sum([1 for row in data for i in row if i == -1])
    pass


def update_after_flash(data):
    # octopus with a neighbour == 0 get a unit increase in energy
    # octopus with a 0 -> -1 to mark as processed
    padded_data = pad_data(data)
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] == 0:  # the octopus flashed
                # increase neighbours energy if they haven't flashed
                coords = list(
                    filter(
                        lambda z: z != (x, y),
                        zip(
                            [x-1, x, x+1]*3,
                            sorted([y-1, y, y+1]*3)
                        )
                    )
                )
                for coord in coords:
                    # 0 flashed in this iteration, -1 if flashed in previous iterations
                    if padded_data[coord[1]+1][coord[0]+1] not in [0, -1]:
                        padded_data[coord[1]+1][coord[0]+1] += 1
    # replace 0 by -1 to avoid processing twice
    return unpad_data(padded_data)
    # return [[-1 if i == 0 else i for i in row] for row in unpad_data(padded_data)]


def part1(data):
    num_steps = 100
    data = [[int(i) for i in row] for row in data]
    total_flashes = 0
    for _ in range(num_steps):
        data = update_after_flash(flash_octopus(update_octopus(data)))
        chain_reaction = True
        while chain_reaction:
            # Mark octopus that have already flashed in this step
            data = [[-1 if i == 0 else i for i in row] for row in data]
            data = update_after_flash(flash_octopus(data))
            # Check if new octopus have flashed in the reaction
            if not 0 in [i for row in data for i in row]:
                chain_reaction = False
        # Update num of flashes
        total_flashes += count_flashes(data)
        data = [[0 if i==-1 else i for i in row] for row in data]
    return total_flashes


def part2(data):
    data = [[int(i) for i in row] for row in data]
    all_flashed = False
    step = 1
    while not all_flashed:
        data = update_after_flash(flash_octopus(update_octopus(data)))
        chain_reaction = True
        while chain_reaction:
            # Mark octopus that have already flashed in this step
            data = [[-1 if i == 0 else i for i in row] for row in data]
            data = update_after_flash(flash_octopus(data))
            # Check if new octopus have flashed in the reaction
            if not 0 in [i for row in data for i in row]:
                chain_reaction = False
        data = [[0 if i==-1 else i for i in row] for row in data]
        if sum(sum(i for i in row) for row in data) == 0:
            all_flashed = True
        else:
            step += 1
    return step



def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
