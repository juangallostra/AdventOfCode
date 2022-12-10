# from utils import parse_input

DAY = 8
YEAR = 2021


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def first(generator):
    return list(generator)[0]


class SevenSegment(str):
    def __new__(cls, segment):
        sorted_segment = ''.join(sorted(segment))
        return str.__new__(cls, sorted_segment)

    def __add__(self, __s: str):
        return SevenSegment(''.join(set(self).union(set(__s))))

    def __sub__(self, __s: str):
        return SevenSegment(''.join(set(self).difference(set(__s))))

    def intersect(self, __s: str):
        return SevenSegment(''.join(set(self).intersection(set(__s))))


def part1(data):
    data = [val.split(' | ')[1].split(' ') for val in data]
    return len([1 for val in data for i in val if len(i) in [2, 3, 4, 7]])


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
    combinations = tuple((val.split(' | ')[0].split(
        ' '), val.split(' | ')[1].split(' ')) for val in data)
    # sort strings
    combinations = tuple((tuple(SevenSegment(a) for a in val[0]), tuple(
        SevenSegment(b) for b in val[1])) for val in combinations)
    # deduce numbers from segments:
    total = 0
    for combination in combinations:
        source = combination[0]
        destination = combination[1]
        number_ = dict()
        number_['1'] = first(filter(lambda x: len(x) == 2, source))
        number_['4'] = first(filter(lambda x: len(x) == 4, source))
        number_['7'] = first(filter(lambda x: len(x) == 3, source))
        number_['8'] = first(filter(lambda x: len(x) == 7, source))
        # get 5 segment combinations:
        seg_5 = [val for val in source if len(val) == 5]
        # check which 5 segment combinations have 4 segments in common with the rest of 5 segment combinations:
        num_3 = first(l for i, l in enumerate(seg_5) if len(
            l - seg_5[(i+1) % 3]) == 1 and len(l - seg_5[(i+2) % 3]) == 1)
        number_['3'] = num_3
        # get unique 6 segment combinations:
        seg_6 = [val for val in source if len(val) == 6]
        num_6 = first(l for l in seg_6 if len(
            l + number_['1']) > len(l))
        number_['6'] = num_6
        # get top right segment:
        t_r = number_['1'] - number_['6']
        # 5 and 2
        seg_5_2 = [val for val in source if (
            len(val) == 5 and len(val + number_['3']) > 5)]
        num_5 = first(i for i in seg_5_2 if t_r not in i)
        num_2 = first(i for i in seg_5_2 if t_r in i)
        number_['5'] = num_5
        number_['2'] = num_2
        horizontal_seg = number_['5'].intersect(number_['2'])
        # get 0 and 9
        seg_0_9 = [val for val in source if len(
            val) == 6 and len(val + number_['6']) > 6]
        num_0 = first(i for i in seg_0_9 if len(horizontal_seg + i) > len(i))
        num_9 = first(i for i in seg_0_9 if len(horizontal_seg + i) == len(i))
        number_['0'] = num_0
        number_['9'] = num_9
        # now get 4 digit number
        dest_number = ''
        for number in destination:
            for key in number_.keys():
                if number == number_[key]:
                    dest_number += key
        total += int(dest_number)
    return total


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
