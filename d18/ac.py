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
            if open_brackets == 5:  # ouuuh explosion
                end = data[i:].find(']')
                explosive = eval(data[i:i+end+1])
                # replace exploding by 0
                data = data[0:i] + '0' + data[i+end+1:]
                # get previous number, add first item of exploded pair and replace
                idx = 1
                if last_number[0] is not None:
                    data = data[0:last_number[1]] + str(
                        last_number[0] + explosive[0]) + data[last_number[1]+len(str(last_number[0])):]
                    idx = len(str(last_number[0] + explosive[0]))
                # get next number
                for j, p in enumerate(data[i+idx:]):
                    if try_get_number(data[i+idx+j:i+idx+j+2]) is not None:
                        # it could be that the next number has 2 digits
                        next_number = (try_get_number(
                            data[i+idx+j:i+idx+j+2]), i+idx+j)
                        data = data[0:next_number[1]] + \
                            str(next_number[0] + explosive[1]
                                ) + data[next_number[1]+2:]
                        break
                    elif try_get_number(p) is not None:
                        # it could be that the next number has 2 digits
                        next_number = (try_get_number(p), i+idx+j)
                        data = data[0:next_number[1]] + \
                            str(next_number[0] + explosive[1]
                                ) + data[next_number[1]+1:]
                        break
                return eval(data)
        elif d == ']':
            open_brackets -= 1
        elif try_get_number(data[i-1:i+1]) is not None:
            last_number = (try_get_number(data[i-1:i+1]), i-1)
        elif try_get_number(d) is not None:
            last_number = (try_get_number(d), i)
    return eval(data)


def split_sn(data):
    # eaaaaasy
    nums = flatten(data)
    data = str(data).replace(' ', '')
    for num in nums:
        if num > 9:
            idx = data.find(str(num))
            data = data[0:idx] + str([math.floor(num/2),
                                     math.ceil(num/2)]) + data[idx+len(str(num)):]
            break
    return eval(data)


def add_nums(num1, num2):
    data = [num1, num2]
    to_c = str(data)
    still_changing = True
    while still_changing:
        # try explode
        data = explode_sn(data)
        if str(data) == to_c:
            # explosion did not happen, try to split
            data = split_sn(data)
            if str(data) == to_c:
                # split did not happen, we are done
                still_changing = False
        to_c = str(data)
    return data


def check_magnitude(result):
    if type(result[0]) is int and type(result[1]) is int:
        return 3 * result[0] + 2 * result[1]
    elif type(result[0]) is list and type(result[1]) is int:
        return 3 * check_magnitude(result[0]) + 2 * result[1]
    elif type(result[1]) is list and type(result[0]) is int:
        return 2 * check_magnitude(result[1]) + 3 * result[0]
    elif type(result[0]) is list and type(result[1]) is list:
        return 3 * check_magnitude(result[0]) + 2 * check_magnitude(result[1])


def part1(data):
    data = [eval(i) for i in data]
    result = data.pop(0)
    for i in data:
        result = add_nums(result, i)
    return check_magnitude(result)


def part2(data):
    data = [eval(i) for i in data]
    max_mag = 0
    for i in range(len(data)):
        for j in range(len(data)):
            # print(i, j)
            if i == j:
                continue
            else:
                result = add_nums(data[i], data[j])
                max_mag = max(max_mag, check_magnitude(result))
    return max_mag


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
