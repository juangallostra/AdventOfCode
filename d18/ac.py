from utils import parse_input

DAY = 18

def flatten(data):
    nums = str(data).replace('[', '').replace(']', '').replace(' ', '')
    return [int(n) for n in nums.split(',')]

def explode_sn(data):
    print(flatten(data))
    exploded = []
    for i, l1 in enumerate(data):
        if isinstance(l1, list):
            for j, l2 in enumerate(l1):
                if isinstance(l2, list):
                    for k, l3 in enumerate(l2):
                        if isinstance(l3, list):
                            for m, l4 in enumerate(l3):
                                # 4 level nested data
                                print(l4) # this explodes

def split_sn(data):
    pass

def part1(data):
    pass


def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
