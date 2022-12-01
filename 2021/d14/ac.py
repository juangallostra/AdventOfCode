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
    ITERATIONS = 10
    template, insertions = get_template_and_insertions(data)
    for _ in range(ITERATIONS):
        to_be_inserted = []
        for idx in range(len(template)):
            if template[idx:idx+2] in insertions.keys():
                to_be_inserted.append(
                    (insertions[template[idx:idx+2]], idx + 1 + len(to_be_inserted)))
        for item in to_be_inserted:
            template = template[:item[1]] + item[0] + template[item[1]:]
    counts = Counter(template)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


def part2(data):
    ITERATIONS = 40
    # idea is to keep a dict of pair -> count that can later be used to count letters.
    # as an example: if NN -> C, then NN -> NC, CN and counts of NN -= 1, NC += 1, CN += 1
    template, insertions = get_template_and_insertions(data)
    all_pairs = tuple(pair for pair in insertions.keys())
    mappings = dict()
    for pair in all_pairs:
        mappings[pair] = [pair[0] + insertions[pair],
                          insertions[pair] + pair[1]]
    # build initial dict of counts from pairs
    # Note: This is not necessarily 1 for each present pair
    splitted = [template[i:i+2] for i in range(len(template))][:-1]
    initial_counts = dict(Counter(splitted))
    counts = {pair: initial_counts.get(pair, 0) for pair in all_pairs}
    # Updated list of counts
    updated_counts = {pair: 0 for pair in all_pairs}
    for _ in range(ITERATIONS):
        # iterate over mappings/counts and update counts
        for current_pair in all_pairs:
            if counts[current_pair] >= 1:  # if pair is present in current template
                for mapping in mappings[current_pair]:  # get insertions
                    updated_counts[mapping] += counts[current_pair]
        counts = {pair: updated_counts[pair] for pair in all_pairs}
        # reset updated counts
        updated_counts = {pair: 0 for pair in all_pairs}
    # To get single letter count -> how many times it appears at the begining of a pair
    # (end of a pair is always the begining of next pair. There are no "dead ends")
    single_letters = set(''.join(pair for pair in all_pairs))
    final_dict = {letter: 0 for letter in single_letters}
    for pair in counts.keys():
        for letter in single_letters:
            if letter == pair[0]:
                final_dict[letter] += counts[pair]
    # Last letter is always the same, since it has no next pair
    final_dict[template[-1]] += 1
    counts = Counter(final_dict)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
