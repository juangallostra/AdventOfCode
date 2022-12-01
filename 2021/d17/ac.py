from utils import parse_input
import math

DAY = 17

def get_target(data):
    targets =  data[0].split(': ')[1].split(', ')
    target_x = [int(x) for x in targets[0].split('=')[1].split('..')] 
    target_y = [int(y) for y in targets[1].split('=')[1].split('..')]
    return (sorted(target_x), sorted(target_y))


def update_pos_and_vel(pos, vel):
    # update position
    for i in range(len(pos)):
        pos[i] += vel[i]
    # update velocity
    vel[1] -= 1
    vel[0] -= vel[0]/abs(vel[0]) if vel[0] != 0 else 0
    # print(f'Pos: {pos}, Vel: {vel}')
    return pos, vel

def find_all_x_vels(x_target):
    target_sorted = sorted(x_target, key = lambda x: abs(x)) # target[0] -> closest to (0,0)
    x_vels = [] # tuple of (x_vel_init, time_to_reach_target)
    # max x vel -> t=1 reaches target farthest extreme
    max_x_vel = (target_sorted[1], 1, False)
    x_vels.append(max_x_vel)
    for x_vel in range(max_x_vel[0]): # assume we always move forward!!
        # see if target is reached and when
        has_stopped = False
        pos = [0, 0]
        vel = [x_vel, 0]
        t = 0
        while not has_stopped:
            pos, vel = update_pos_and_vel(pos, vel)
            t += 1
            if x_target[0] <= pos[0] <= x_target[1]:
                if vel[0] == 0:
                    x_vels.append((x_vel, t, True))
                else:
                    x_vels.append((x_vel, t, False))
            if vel[0] == 0:
                has_stopped = True
    return sorted(x_vels, key=lambda x: x[0])

def find_range_y_vels(y_target):
    target_sorted = sorted(y_target, key = lambda y: abs(y)) # target[0] -> closest to (0,0)
    y_vels = [] # tuple of (y_vel_init, time_to_reach_target)
    # max x vel -> t=1 reaches target farthest extreme
    min_y_vel = target_sorted[1] # assume y is always negative
    max_y_vel = (target_sorted[1] + 1) * (-1)
    y_vels.append(min_y_vel)
    y_vels.append(max_y_vel)
    return y_vels

def part1(data):
    target = get_target(data)
    # assuming y target is always negative:
    # max y' is when at y=0 y'=y_target[1], being y_target[1] the farthest y from (0,0)
    # when this is the case, the y'_initial = (y_target[1] + 1)*(-1)
    max_y_vel = (target[1][0] + 1) * -1
    return max_y_vel * (max_y_vel + 1)/2 # max height: sum from 0 to max_y_vel


def part2(data):
    target = get_target(data)
    # get all y velocities and time to reach target
    x_vels = find_all_x_vels(target[0])
    y_vels = find_range_y_vels(target[1])
    # find which combinations of y and x vels will reach target at the same time
    vel_pairs = []
    for y_vel in range(y_vels[0], y_vels[1] + 1):
        # For each y velocity in the range check if there is an 
        # x velocity that will reach the target at the same time
        # There are 2 possibilities: equal t or v_x = 0 inside target and ty > tx
        target_overshot = False
        pos = [0, 0]
        vel = [0, y_vel]
        t = 0
        while not target_overshot:
            pos, vel = update_pos_and_vel(pos, vel)
            t += 1
            if target[1][0] <= pos[1] <= target[1][1]:
                # inside target
                for x_vel, t_x, stopped in x_vels:
                    # equal time
                    if (x_vel, y_vel) in vel_pairs:
                        continue
                    elif t_x == t:
                        vel_pairs.append((x_vel, y_vel))
                    elif stopped and t_x < t:
                        vel_pairs.append((x_vel, y_vel))
            elif pos[1] < target[1][0]:
                target_overshot = True
    return len(vel_pairs)


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
