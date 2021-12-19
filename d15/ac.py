from utils import parse_input

DAY = 15


def add_node_to_path(path, coord):
    new_path = path.clone()
    new_path.add_node(coord)
    return new_path


class Node:
    def __init__(self, x, y, score) -> None:
        self._x = x
        self._y = y
        self._score = score

    @property
    def score(self):
        return self._score

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Path():
    def __init__(self, path=None) -> None:
        if path is None:
            self._path = []
        else:
            self._path = path

    @property
    def score(self):
        return sum([node.score for node in self._path])

    @property
    def path_endpoint(self):
        return self._path[-1]

    @property
    def path(self):
        return self._path

    def add_node(self, node):
        self._path.append(node)

    def add_node_from_raw_values(self, x, y, score):
        self.add_node(Node(x, y, score))

    @property
    def coords(self):
        return [(node.x, node.y) for node in self._path]

    def clone(self):
        return Path([node for node in self._path])

    # Compare paths based on score
    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __ne__(self, other):
        return self.score != other.score
    
    def __repr__(self):
        return ','.join([f'({node.x}, {node.y})' for node in self._path])



DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def part1(data):
    data = [[int(i) for i in row] for row in data] # map data
    init = Node(0, 0, 0) # initial node
    target = (len(data[0])-1, len(data)-1)  # target coordinates (x,y)
    # candidate paths
    paths = [Path([init])]  # this list has to be kept sorted
    # idea is to keep a sorted list of paths, and keep extending the shortest path until the end is reached
    target_reached = False
    shortest_path = None
    visited = []
    while not target_reached:
        # deque shortest path
        path = paths.pop(0)
        # Extend shortest path in 4 directions
        for direction in DIRECTIONS:
            # get next node
            next_x = path.path_endpoint.x + direction[0]
            next_y = path.path_endpoint.y + direction[1]
            # idea: keep track of visited nodes
            if next_x < 0 or next_x >= len(data[0]):
                continue 
            if next_y < 0  or next_y >= len(data):
                continue
            if (next_x, next_y) in visited:
                continue
            node = Node(next_x, next_y, data[next_y][next_x])
            visited.append((next_x, next_y))
            # Add to paths
            extended_path = add_node_to_path(path, node)
            paths.append(extended_path)
            if node.x == target[0] and node.y == target[1]:
                target_reached = True
                shortest_path = extended_path
                break
        # sort paths by score
        paths = sorted(paths)
    return shortest_path.score

def part2(data):
    data = [[int(i) for i in row] for row in data]
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
