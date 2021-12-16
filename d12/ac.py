from utils import parse_input
from collections import Counter

DAY = 12

# Part 1
# All paths from start to end. Big caves (CAPS) can be visited more than once, small caves only once.

# Part 2
# a single small cave (different from start and end) can be visited twice.

def get_connections(data):
    """Build a graph of all the connections between the rooms."""
    connections = dict()
    for passage in data:
        start, end = passage.split('-')
        if start in connections.keys():
            connections[start].append(end)
        else:
            connections[start] = [end]
        if end in connections.keys():
            connections[end].append(start)
        else:
            connections[end] = [start]
    return connections

def already_duplicate_small_room(path):
    counts = Counter(path)
    return any(counts[k] > 1 for k in [k for k in counts.keys() if (k.islower() and k not in ['start', 'end'])])

def part1(data):
    current = 'start'
    target = 'end'
    connections = get_connections(data)
    valid_paths = []
    paths_to_explore = [[current]]
    while paths_to_explore:
        # process next path
        current_path = paths_to_explore.pop(0)
        # grow path. Get next step candidates
        candidates = connections[current_path[-1]]
        # process each candidate room
        for room in candidates:
            # valid candidate: CAPS room or unvisited small room. If valid, add to path
            if room.isupper() or (room.islower() and room not in current_path):
                if room == target:
                    valid_paths.append(current_path + [room])
                # Add a new path to explore
                else:
                    paths_to_explore.append(current_path + [room]) 
    return len(valid_paths)


def part2(data):
    current = 'start'
    target = 'end'
    connections = get_connections(data)
    valid_paths = []
    paths_to_explore = [[current]]
    while paths_to_explore:
        # process next path
        current_path = paths_to_explore.pop(0)
        # grow path. Get next step candidates
        candidates = connections[current_path[-1]]
        # process each candidate room
        for room in candidates:
            # valid candidate: CAPS room, unvisited small room or small room and no repeated small room. If valid, add to path
            if room != 'start' and (room.isupper() or (room.islower() and room not in current_path) or not already_duplicate_small_room(current_path)):
                if room == target:
                    valid_paths.append(current_path + [room])
                # Add a new path to explore
                else:
                    paths_to_explore.append(current_path + [room])
    return len(valid_paths)


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
