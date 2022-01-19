#!/usr/bin/python3

### DAY 17 --- 1 and 2
'''
The probe start position (S) is (0,0).
In each step occurs the following:
    Probe's x position increases by its x velocity.
    Probe's y position increases by its y velocity.
    x velocity changes by 1 towards 0 in each step. If x is + decreases, if it's -, increases, if it's 0 does not change.
    y velocity decreases by 1 in each step.
Part 1: Find the max y value that a trajectory falling in the target area could reach.
Part 2: Find any initial velocities that at any step make the probe fall into the target area.
'''

def read_input(file):
    with open(file,'r') as f:
        for line in f.readlines():
            xmin, xmax = int(line.split(' ')[2].split('=')[1].strip(',').split('..')[0]), int(line.split(' ')[2].split('=')[1].strip(',').split('..')[1])
            ymin, ymax = int(line.split(' ')[3].split('=')[1].strip().split('..')[0]), int(line.split(' ')[3].split('=')[1].strip().split('..')[1])
    return xmin, xmax, ymin, ymax

def part1(y1):
    vy = -y1-1
    ymax = (abs(vy)*(abs(vy)+1))/2 # n*(n-1)/2 formula from subreddit
    return ymax

def part2(x0, x1, y0, y1):
    ymax = max(abs(y0),abs(y1))
    velocity_counter = 0
    for vel_x in range(x1+1):
        for vel_y in range(-ymax, ymax+1):
            x, y = 0, 0
            vx,vy = vel_x, vel_y
            while True:
                # these 3 breaking conditions should be checked for another input
                if x > x1: break
                if x < x0 and vx == 0: break
                if y < y0: break

                if x0 <= x <= x1 and y0 <= y <= y1:
                    velocity_counter += 1
                    break
                x += vx
                y += vy
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
    return velocity_counter


if __name__ == "__main__":
    file = 'input.txt'
    xmin, xmax, ymin, ymax = read_input(file)
    # print(xmin, xmax, ymin, ymax)
    print('Max y is:', int(part1(ymin)))
    print(part2(xmin, xmax, ymin, ymax), 'different velocities')