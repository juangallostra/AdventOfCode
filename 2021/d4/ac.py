from utils import parse_input

DAY = 4

class Cell():
    def __init__(self, value, checked=False):
        self.value = value
        self.checked = checked

class Board():
    def __init__(self, values):
        self.winning_position = 0
        self.has_won = False
        self.last_call = -1
        self.values = [[Cell(int(i)) for i in row.split()] for row in values]

    def check_cols(self):
        cols =[[self.values[row_idx][col_idx].checked for row_idx in range(len(self.values))] for col_idx in range(len(self.values[0]))]
        # Check if any col has all cells set to True
        all_true = [idx for idx in range(len(cols)) if all(cols[idx])]
        if len(all_true) > 0:
            return all_true[0]
        return -1

    def check_rows(self):
        # Check if any col has all cells set to True
        all_true = [idx for idx in range(len(self.values)) if all([c.checked for c  in self.values[idx]])]
        if len(all_true) > 0:
            return all_true[0]
        return -1

    def check_win(self):
        return self.check_rows() != -1 or self.check_cols() != -1

    def update_board(self, value):
        for cell in [cell for row in self.values for cell in row]:
            if cell.value == value:
                cell.checked = True
                self.last_call = value
                break

    def get_score(self, last_call):
        p1_score = sum([c.value for row in self.values for c in row if not c.checked])
        return p1_score * last_call


def part1(data):
    called = data[0]
    boards = data[1]
    for num in called:
        for board in boards:
            board.update_board(num)
            if board.check_win():
                return board.get_score(num)

def part2(data):
    # Get Last winning board and return its score
    winning_position = 0
    called = data[0]
    boards = data[1]
    num_called_idx = 0
    while num_called_idx < len(called)-1 and len([b for b in boards if not b.has_won]) > 0:
        for board in [b for b in boards if not b.has_won]:
            board.update_board(called[num_called_idx])
            if board.check_win():
                board.has_won = True
                board.winning_position = winning_position
                winning_position += 1
        num_called_idx += 1
    # Get last winning board
    last_board = sorted([b for b in boards if b.has_won], key=lambda x: x.winning_position)[-1]
    return last_board.get_score(last_board.last_call)


def main(input_file):
    data = parse_input(input_file)
    called = [int(i) for i in data[0].split(',')] # Called numbers
    boards = [Board(data[i+1:i+6]) for i in range(len(data)) if data[i] == '']
    # Further data processing
    print(f'Part1: {part1([called, boards])}')
    print(f'Part2: {part2([called, boards])}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
