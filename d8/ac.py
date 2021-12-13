from utils import parse_input

DAY = 8


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
    # TODO: Rework, this is super ugly. Just by sorting strings code should become much more readable
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
        number_to_segments = dict()
        number_to_segments['1'] = [val for val in source if len(val) == 2][0]
        number_to_segments['4'] = [val for val in source if len(val) == 4][0]
        number_to_segments['7'] = [val for val in source if len(val) == 3][0]
        number_to_segments['8'] = [val for val in source if len(val) == 7][0]
        # get 5 segment combinations:
        seg_5 = [val for val in source if len(val) == 5]
        # check which 5 segment combinations have 4 segments in common with the rest of 5 segment combinations:
        num_3 = [l for i, l in enumerate(seg_5) if len(
            l - seg_5[(i+1) % 3]) == 1 and len(l - seg_5[(i+2) % 3]) == 1][0]
        number_to_segments['3'] = num_3
        # get unique 6 segment combinations:
        seg_6 = [val for val in source if len(val) == 6]
        num_6 = [l for l in seg_6 if len(
            l + number_to_segments['1']) > len(l)][0]
        number_to_segments['6'] = num_6
        # get top right segment:
        t_r = [a for a in number_to_segments['1']
               if a not in number_to_segments['6']][0]
        # 5 and 2
        seg_5_2 = [val for val in source if (
            len(val) == 5 and len(val + number_to_segments['3']) > 5)]
        num_5 = [i for i in seg_5_2 if t_r not in i][0]
        num_2 = [i for i in seg_5_2 if t_r in i][0]
        number_to_segments['5'] = num_5
        number_to_segments['2'] = num_2
        horizontal_seg = SevenSegment(''.join([l for l in number_to_segments['5'].intersect(
            number_to_segments['2'])]))
        # get 0 and 9
        seg_0_9 = [val for val in source if len(
            val) == 6 and len(val + number_to_segments['6']) > 6] 
        num_0 = [i for i in seg_0_9 if len(horizontal_seg + i) > len(i)][0]
        num_9 = [i for i in seg_0_9 if len(horizontal_seg + i) == len(i)][0]
        number_to_segments['0'] = num_0
        number_to_segments['9'] = num_9
        # now get 4 digit number
        dest_number = ''
        for number in destination:
            for key in number_to_segments.keys():
                if number == number_to_segments[key]:
                    dest_number += key
        total += int(dest_number)
    return total


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
