from utils import parse_input

DAY = 10

def remove_match(matches, data):
    for match in matches:
        if match in data:
            return remove_match(matches, data.replace(match, ''))
    return data

SCORES_CORRUPTED = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}

SCORES_COMPLETION = {
    '(': 1, '[': 2, '{': 3, '<': 4
}

MATCHES = ['<>', '{}', '()', '[]']
def part1(data):
    total = 0
    for line in data:
        processed = remove_match(MATCHES, line)
        # look for first illegal character
        for c in processed:
            if c in SCORES_CORRUPTED.keys():
                total += SCORES_CORRUPTED[c]
                break
    return total                
          

def part2(data):
    scores = []
    for line in data:
        processed = remove_match(MATCHES, line)
        # look for first illegal character
        corrupted = any(c in processed for c in SCORES_CORRUPTED.keys())
        if not corrupted:
            score = 0
            for c in processed[::-1]: # reverse since we are closing
                score = score*5 + SCORES_COMPLETION[c]
            scores.append(score)
    return sorted(scores)[len(scores)//2]   


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
