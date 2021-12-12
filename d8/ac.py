from utils import parse_input

DAY = 8


def part1(data):
    data = [val.split(' | ')[1].split(' ') for val in data]
    return len([1 for val in data for i in val if len(i) in [2,3,4,7]])



def part2(data):
    """
    * 1,4,7,8 -> unique number of segments, easy to know
    * 3 -> 5 segment combination which has 4 segments in common with the rest of 5 segment combinations
    * 6 -> unique 6 segment which does not have a segment from number 1
    * from 6 and 1 -> get top right segment
    * from top right segment differentiate 5 and 2 (2 has it, 5 no)
    * from 2 and 5, get all horizontal segments
    * 9 has all horizontal segments, 0 doesn't
    """
    combinations = [(val.split(' | ')[0].split(' '), val.split(' | ')[1].split(' '))  for val in data]
    # deduce numbers from segments:
    total = 0
    for combination in combinations:
        source = combination[0]
        destination = combination[1]
        number_to_segments = dict()
        number_to_segments['1'] = [[l for l in val] for val in source if len(val) == 2][0]
        number_to_segments['4'] = [[l for l in val] for val in source if len(val) == 4][0]
        number_to_segments['7'] = [[l for l in val] for val in source if len(val) == 3][0]
        number_to_segments['8'] = [[l for l in val] for val in source if len(val) == 7][0]
        # get 5 segment combinations:
        seg_5 = [[l for l in val] for val in source if len(val) == 5]
        # check which 5 segment combinations have 4 segments in common with the rest of 5 segment combinations:
        num_3 = [l for i, l in enumerate(seg_5) if len(set(l).intersection(set(seg_5[(i+1)%3]))) == 4 and len(set(l).intersection(set(seg_5[(i+2)%3]))) == 4][0]
        number_to_segments['3'] = num_3
        # get unique 6 segment combinations:
        seg_6 = [[l for l in val] for val in source if len(val) == 6]
        num_6 = [l for l in seg_6 if len(set(l).intersection(set(number_to_segments['1'][0]))) == 0 or len(set(l).intersection(set(number_to_segments['1'][1]))) == 0][0]
        number_to_segments['6'] = num_6
        # get top right segment:
        t_r = [a for a in number_to_segments['1'] if a not in number_to_segments['6']][0]
        # 5 and 2
        seg_5_2 = [[l for l in val] for val in source if (len(val) == 5 and len(set([l for l in val]).union(set(number_to_segments['3'])))>5)]
        num_5 = [i for i in seg_5_2 if t_r not in i][0]
        num_2 = [i for i in seg_5_2 if t_r in i][0]
        number_to_segments['5'] = num_5
        number_to_segments['2'] = num_2
        horizontal_seg = [l for l in set(number_to_segments['5']).intersection(set(number_to_segments['2']))]
        # get 0 and 9
        seg_0_9 = [[l for l in val] for val in source if len(val) == 6 and len(set([l for l in val]).union(set(number_to_segments['6'])))>6]
        num_0 = [i for i in seg_0_9 if not set(horizontal_seg).issubset(set(i).intersection(set(horizontal_seg)))][0]
        num_9 = [i for i in seg_0_9 if set(horizontal_seg).issubset(set(i).intersection(set(horizontal_seg)))][0]
        number_to_segments['0'] = num_0
        number_to_segments['9'] = num_9
        # now get 4 digit number
        dest_number = ''
        for number in destination:
            for key in number_to_segments.keys():
                if len(number) == len(number_to_segments[key]) and sum([1 for i in number if i in number_to_segments[key]]) == len(number_to_segments[key]):
                    dest_number += key
        total += int(dest_number)
    return total

def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
