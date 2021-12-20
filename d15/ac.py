from utils import parse_input

DAY = 15


def add_node_to_path(path, coord):
    new_path = path.clone()
    new_path.add_node(coord)
    return new_path


def get_node_at_position(data, x, y):
    """
    There is no need to compute the whole map, knowing x and y the score can be computed
    """
    x_offset = x // len(data[0])  # multiplier for x
    y_offset = y // len(data)     # multiplier for y
    cell_x = x % len(data[0])  # offset for x
    cell_y = y % len(data)    # offset for y
    abs_score = data[cell_y][cell_x] + x_offset + y_offset
    score = abs_score % 9 if abs_score % 9 != 0 else 9
    return Node(x, y, score)


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

    def __repr__(self) -> str:
        return f'Last node: ({self.x}, {self.y}); Score: {self.score})'


class Path():
    """
    This path only keeps track of its last node and the current score as
    opposed to the whole path information
    """

    def __init__(self, node, score) -> None:
        self._node = node
        self._score = score

    @property
    def score(self):
        return self._score

    @property
    def node(self):
        return self._node

    def update_path_endpoint(self, node):
        return Path(Node(node.x, node.y, node.score), self._score + node.score)

    def __repr__(self) -> str:
        return f'Path: ({self._node.x}, {self._node.y}), {self.score})'

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


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def part1(data):
    data = [[int(i) for i in row] for row in data]  # map data
    init = Node(0, 0, 0)  # initial node
    target = (len(data[0])-1, len(data)-1)  # target coordinates (x,y)
    # candidate paths
    paths = [Path(init, 0)]  # this list has to be kept sorted
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
            next_x = path.node.x + direction[0]
            next_y = path.node.y + direction[1]
            # idea: keep track of visited nodes
            if next_x < 0 or next_x >= len(data[0]):
                continue
            if next_y < 0 or next_y >= len(data):
                continue
            if (next_x, next_y) in visited:
                continue
            node = Node(next_x, next_y, data[next_y][next_x])
            visited.append((next_x, next_y))
            # extend path and add to list
            extended_path = path.update_path_endpoint(node)
            paths.append(extended_path)
            if node.x == target[0] and node.y == target[1]:
                target_reached = True
                shortest_path = extended_path
                break
        # sort paths by score
        paths = sorted(paths)
    return shortest_path.score


def part2(data):
    # There is a set of optimizations we can do here
    # Another approach that comes to mind is to keep a track of
    # which is the smallest score required to reach a node.
    # We don't actually need to keep track of the path, just the last node
    # of the path and the smallest score required to reach it. (?)
    CELLS = 5
    data = [[int(i) for i in row] for row in data]  # map data
    init = Node(0, 0, 0)  # initial node
    target = (
        len(data[0])*CELLS-1, len(data)*CELLS-1
    )  # target coordinates (x,y)
    # candidate paths
    paths = [Path(init, 0)]  # this list has to be kept sorted
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
            next_x = path.node.x + direction[0]
            next_y = path.node.y + direction[1]
            # idea: keep track of visited nodes
            if next_x < 0 or next_x >= len(data[0])*CELLS:
                continue
            if next_y < 0 or next_y >= len(data)*CELLS:
                continue
            if (next_x, next_y) in visited:
                continue
            node = get_node_at_position(data, next_x, next_y)
            # node = Node(next_x, next_y, data[next_y][next_x])
            visited.append((next_x, next_y))
            # Add to paths
            extended_path = path.update_path_endpoint(node)
            # extended_path = add_node_to_path(path, node)
            paths.append(extended_path)
            if node.x == target[0] and node.y == target[1]:
                target_reached = True
                shortest_path = extended_path
                break
        # sort paths by score
        # I guess this can be optimised: we can append the path at the correct position
        paths = sorted(paths)
    return shortest_path.score


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
