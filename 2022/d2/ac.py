from typing import List


DAY = 2
YEAR = 2022

player_score = {
    'R': 1,
    'P': 2,
    'S': 3
}

game_points = {
    0: 3,
    -1: 0,
    2: 0,
    1: 6,
    -2: 6
}

game_points_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

move = {
    'X': 1,
    'Y': 0,
    'Z': -1,
}

game_moves = ['S', 'P', 'R']


def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements


def map_game_to_rps(game: str) -> str:
    return game.replace('A', 'R').replace('B', 'P').replace(
        'C', 'S').replace('X', 'R').replace('Y', 'P').replace('Z', 'S')


def get_player_score(game):
    idx = (game_moves.index(map_game_to_rps(game[0])) +
           move[game[-1]]) % len(game_moves)
    return player_score[game_moves[idx]]


def part1(data: List[str]):
    return sum(
        [
            game_points[
                game_moves.index(map_game_to_rps(game[0])) -
                game_moves.index(map_game_to_rps(game[-1]))
            ] +
            player_score[
                map_game_to_rps(game[-1])
            ]
            for game in data
        ]
    )


def part2(data):
    return sum(
        [
            game_points_2[game[-1]] + get_player_score(game) for game in data
        ]
    )


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'{YEAR}/d{DAY}/data/input.txt')
