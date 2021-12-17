from utils import parse_input
from collections import Counter


DAY = 14

def get_template_and_insertions(data):
    template = ''
    insertions = dict()
    for line in data:
        if '->' in line:
            insertion = line.split(' -> ')
            insertions[insertion[0]] = insertion[1]
        elif not line:
            continue
        else:
            template = line
    return template, insertions

def part1(data):
    template, insertions = get_template_and_insertions(data)
    for _ in range(10):
        to_be_inserted = []
        for idx in range(len(template)):
            if template[idx:idx+2] in insertions.keys():
                to_be_inserted.append((insertions[template[idx:idx+2]], idx + 1 + len(to_be_inserted)))
        for item in to_be_inserted:
            template = template[:item[1]] + item[0] + template[item[1]:]
    counts = Counter(template)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]
    
       

def part2(data):
    template, insertions = get_template_and_insertions(data)
    for i in range(40):
        print(i)
        to_be_inserted = []
        for idx in range(len(template)):
            if template[idx:idx+2] in insertions.keys():
                to_be_inserted.append((insertions[template[idx:idx+2]], idx + 1 + len(to_be_inserted)))
        for item in to_be_inserted:
            template = template[:item[1]] + item[0] + template[item[1]:]
    counts = Counter(template)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]



def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
