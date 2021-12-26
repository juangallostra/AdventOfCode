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

def find_x_vels(optimal_x_vel, target):
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
    return candidates

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

def find_all_y_vels(y_target):
    target_sorted = sorted(y_target, key = lambda y: abs(y)) # target[0] -> closest to (0,0)
    y_vels = [] # tuple of (y_vel_init, time_to_reach_target)
    # max x vel -> t=1 reaches target farthest extreme
    min_y_vel = (target_sorted[1], 1) # assume y is always negative
    y_vels.append(min_y_vel)
    # for x_vel in range(max_x_vel[0]):
    #     # see if target is reached and when
    #     has_stopped = False
    #     pos = [0, 0]
    #     vel = [x_vel, 0]
    #     t = 0
    #     while not has_stopped:
    #         pos, vel = update_pos_and_vel(pos, vel)
    #         t += 1
    #         if x_target[0] <= pos[0] <= x_target[1]:
    #             if vel[0] == 0:
    #                 x_vels.append((x_vel, t, True))
    #             else:
    #                 x_vels.append((x_vel, t, False))
    #         if vel[0] == 0:
    #             has_stopped = True
    # return sorted(x_vels, key=lambda x: x[0])

def part1(data):
    # TODO: This solution is overkill and pretty much suboptimal.
    # TODO: There are many things that shouldn't be here and are not necessary
    # TODO: Since x and y are independent, it is way easier to just compute the max y velocity 
    # that will pass through the y target range. There will always be an x velocity that will
    # also pass through the x target range at the same time. 
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
    final_vel = 0
    # target = [target[0], sorted(target[1], key = lambda x: abs(x))]
    for vel_set in min_vels:
        vel_y = vel_set[1]
        # keep_trying = True
        i = 0
        # while keep_trying:
        # as always, bruteforce solution...
        while i < 1000:
            target_hit_or_overshot = False
            pos = [0, 0]
            vel = [vel_set[0], vel_y]
            i+=1
            while not target_hit_or_overshot:
                pos, vel = update_pos_and_vel(pos, vel)
                if target[1][0] <= pos[1] <= target[1][1]:
                    print( target[1][0],pos[1],target[1][1])
                    target_hit_or_overshot = True
                    if final_vel < vel_y:
                        final_vel = vel_y
                    print(pos, vel, vel_y)
                    vel_y += 1
                elif pos[1] <= target[1][0]:
                    target_hit_or_overshot = True
                    vel_y += 1
                    # keep_trying = False
    return final_vel * (final_vel + 1)/2


def part2(data):
    target = get_target(data)
    # get all y velocities and time to reach target
    # y_vels = get_all_y_vels(target)
    x_vels = find_all_x_vels(target[0])
    print(x_vels)
    y_vels = find_all_y_vels(target[1])
    # find which combinations of y and x vels will reach target at the same time
    pass
    # x_accel = -1
    # target = get_target(data)
    # # optimal_t = get_optimal_t(target[0], accel=x_accel)
    # # find viable t closest to optimal t
    # # optimal_x_vel = -x_accel * optimal_t
    # x_vel = find_x_vels(optimal_x_vel, target[0])
    # print(x_vel)
    # # now that i know how much time i have available and the target y positions, 
    # # compute y velocities that hit the target at the same time that any x_velocity?
    # x_times = set([c[1] for c in x_vel])
    # print(x_times)



def main(input_file):
    data = parse_input(input_file)
    # print(f'Part1: {part1(data)}')
    print(f'Part2: {part2(data)}')


if __name__ == '__main__':
    main(f'd{DAY}/data/input.txt')
