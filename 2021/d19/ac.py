import math
from utils import parse_input

DAY = 19
YEAR = 2021


class Beacon():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __str__(self) -> str:
        return f'Beacon at: ({self.x}, {self.y}, {self.z})\n'

    def __repr__(self) -> str:
        return str(self)


class Scanner():
    def __init__(self, scanner_idx, detected_beacons) -> None:
        self.idx = scanner_idx
        self.detected_beacons = detected_beacons


def parse_input(data):
    scanners = []
    current_scanner = -1
    beacons = []
    for line in data:
        if "---" in line:  # scanner
            current_scanner = int(line.replace(
                '---', '').replace('scanner', ''))
            if current_scanner > 0:
                scanners.append(Scanner(current_scanner - 1, beacons))
            beacons = []
        else:
            data = line.split(',')
            if len(data) == 3:
                beacons.append(Beacon(*[int(a) for a in line.split(',')]))
    scanners.append(Scanner(current_scanner, beacons))
    return scanners


def part1(data):
    scanners = parse_input(data)
    for scanner in scanners:
        pass


def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
