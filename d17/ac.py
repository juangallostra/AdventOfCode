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


def get_optimal_t(target, accel=-1):
    # optimal time is given when v = 0 and x = farthest from origin
    x_farthest = target[0] if abs(target[0]) > abs(target[1]) else target[1]
    return math.sqrt((-2 * x_farthest)/accel)


def find_candidate_x_vels(optimal_x_vel, target):
    v_init = int(optimal_x_vel)
    candidates = []
    keep_checking = True
    while keep_checking:
        # new set
        pos = [0, 0]
        vel = [v_init, 0]
        t = 0
        target_reached = False
        while vel[0] > 0:
            pos, vel = update_pos_and_vel(pos, vel)
            t += 1
            if target[0] <= pos[0] <= target[1]:
                candidates.append((v_init, t))
                target_reached = True
        if not target_reached:
            keep_checking = False
        else:
            v_init -= 1
    # keep only best candidate for each vel
    vels = set(i[0] for i in candidates)
    best_candidates = tuple([tuple([i, max([c[1] for c in candidates if c[0]==i])]) for i in vels]) 
    return best_candidates


def part1(data):
    x_accel = -1
    target = get_target(data)
    optimal_t = get_optimal_t(target[0], accel=x_accel)
    # find viable t closest to optimal t
    optimal_x_vel = -x_accel * optimal_t
    x_vel = find_candidate_x_vels(optimal_x_vel, target[0])
    # now that i know how much time i have available and the target y positions, compute optimal y velocity?
    min_vels = []
    for t in [c[1] for c in x_vel]:
        # just compute worst case, i.e y closer to 0
        y = sorted(target[1], key = lambda x: abs(x))[0]
        # find min y_0 to reach target at t. However, we can do better
        # i guess we don't care about x_vels because they end up being all 0 (?)
        # should we keep track of them?
        min_vels.append([t, math.ceil((y - (1/2)*(-1)*t**2)/t)])
    # grow y until target is not reached
    print(min_vels)
    for vel_set in min_vels:
        pass

def part2(data):
    pass


def main(input_file):
    data = parse_input(input_file)
    print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/test_input.txt')
