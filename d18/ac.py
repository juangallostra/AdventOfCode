from utils import parse_input
import math

DAY = 18

def flatten(data):
    nums = str(data).replace('[', '').replace(']', '').replace(' ', '')
    return [int(n) for n in nums.split(',')]

def try_get_number(num):
    try:
        return int(num)
    except:
        return None

def explode_sn(data):
    data = str(data).replace(' ', '')
    open_brackets = 0
    last_number = (None, 0)
    # problem of working with strings is that 
    # I have to rebuild the expression?
    for i, d in enumerate(data):
        if d == '[':
            open_brackets += 1
            if open_brackets == 5: # ouuuh explosion
                explosive = eval(data[i:i+5])
                data = data[0:i] + '0' + data[i+5:] # replace exploding by 0
                # get previous number, add first item of exploded pair and replace
                if last_number[0] is not None:
                    data = data[0:last_number[1]] + str(last_number[0] + explosive[0]) + data[last_number[1]+1:]
                # get next number
                for j, p in enumerate(data[i+1:]):
                    if try_get_number(p):
                        next_number = (try_get_number(p), i+1+j)
                        data = data[0:next_number[1]] + str(next_number[0] + explosive[1]) + data[next_number[1]+1:]
                        break
                return eval(data)
        elif d == ']':
            open_brackets -= 1
        elif try_get_number(d):
                last_number = (try_get_number(d), i)

def split_sn(data):
    # eaaaaasy
    nums = flatten(data)
    data = str(data).replace(' ', '')
    for num in nums:
        if num > 9:
            # str([math.floor(num/2),math.ceil(num/2)]))
            idx = data.find(str(num))
            data = data[0:idx] + str([math.floor(num/2),math.ceil(num/2)]) + data[idx+len(str(num)):]
            break
    return eval(data)


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
