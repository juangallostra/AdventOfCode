from utils import parse_input

DAY = 6


def parse_data(data):
    return [int(i) for i in data[0].split(',')]


def next_day(data, days):
    if days > 0:
        m = []
        for i in data:
            if i-1 >= 0:
                m.append(i-1)
            else:
                m += [6, 8]
        return next_day(m, days-1)
    return data


def spawned_fishes(fish, days):
    # build an array of (day, spawns)
    bank = {fish: 1}
    days_to_process = [i for i in bank.keys()]
    short_spawn = 7
    long_spawn = 9
    while days_to_process:
        new_days_to_process = []
        day = days_to_process.pop(0)
        # Add spawns if spawn day lies inside the range
        if day < days:
            try:
                bank[day + short_spawn] += bank[day]
            except KeyError:
                bank[day + short_spawn] = bank[day]
            new_days_to_process.append(day + short_spawn)
            try:
                bank[day + long_spawn] += bank[day]
            except KeyError:
                bank[day + long_spawn] = bank[day]
            new_days_to_process.append(day + long_spawn)
        days_to_process = set(days_to_process).union(set(new_days_to_process))
        # Filter out days that are outside the range
        days_to_process = [day for day in days_to_process if day <= days]
        # sort by day
        days_to_process = sorted(days_to_process)
    # keep only terminal nodes
    keys_to_keep = [k for k in bank.keys() if k >= days]
    return sum([bank[k] for k in keys_to_keep])



def part1(data):
    data = parse_data(data)
    return len(next_day(data, 80))


def part2(data):
    # Idea -> keep track of how many fish spawn each day
    data = parse_data(data)    
    total = 0
    for fish in data:
        total += spawned_fishes(fish, 256)
    return total


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
