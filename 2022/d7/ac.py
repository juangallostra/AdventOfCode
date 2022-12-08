from dataclasses import dataclass
from typing import List, Union


DAY = 7
YEAR = 2022


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


@dataclass
class Node:
    name: str
    size: Union[int, None]
    parent: ...  # Node or None
    children: ...

    def draw(self, indentation_level=0) -> str:
        if self.children:
            return '  ' * indentation_level + f'{self.name} - {self.size}\n' + '\n'.join([c.draw(indentation_level+1) for c in self.children])
        return '  ' * indentation_level + f'{self.name} - {self.size}'


def build_tree(data):
    clean_data: List[str] = [d for d in data if d !=
                             '$ ls' and 'dir' not in d]  # remove unnecessary lines
    # build tree
    current_dir: Union[Node, None] = None
    tree: Union[Node, None] = None
    for line in clean_data:
        if line == '$ cd ..':  # move to parent
            current_dir = current_dir.parent
        elif '$ cd' in line:  # move to a new dir
            new_dir = Node(line.strip('$ cd '), current_dir, list(), 0)
            if tree is None:
                tree = new_dir
            # Update tree
            if current_dir is not None:
                current_dir.children.append(new_dir)
            current_dir = new_dir
        else:  # file
            f_size, f_name = line.split()
            new_file = Node(f_name, current_dir, None, int(f_size))
            current_dir.children.append(new_file)
            # Propagate sum upwards ?
            up_push = new_file.parent
            while up_push is not None:
                up_push.size += int(f_size)
                up_push = up_push.parent
    return tree


def part1(data):
    tree = build_tree(data)
    # print(tree.draw())
    # sum dirs that have a size <= 100000
    to_visit = [tree]
    dir_sum = 0
    # visit all nodes and check
    while to_visit:
        # visit node
        current_node = to_visit.pop()
        if current_node.children is not None:  # ignore files
            if current_node.size <= 100_000:
                dir_sum += current_node.size  # add size and forget
            if current_node.children:
                # update nodes to visit
                to_visit += [c for c in current_node.children if c.children is not None]

    return dir_sum


def part2(data):
    tree = build_tree(data)
    free = 70_000_000 - tree.size
    required = 30_000_000 - free
    # find smallest dir such that, if deleted
    to_visit = [tree]
    dir_size = None
    # visit all nodes and check
    while to_visit:
        # visit node
        current_node = to_visit.pop()
        if current_node.children is not None:  # ignore files
            if current_node.size >= required and (dir_size is None or current_node.size <= dir_size):
                dir_size = current_node.size
            if current_node.children:
                # update nodes to visit
                to_visit += [c for c in current_node.children if c.children is not None]

    return dir_size


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
