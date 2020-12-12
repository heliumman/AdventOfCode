import common
import math

LEFT = -1
RIGHT = 0

def main() :
    dat = common.readFile('day12.dat')

    end_pos = travers_directions(dat)
    print(abs(end_pos[0]) + abs(end_pos[1]))

    waypoint = [10, 1]


def travers_directions(dat):
    waypoint = [10, 1]
    pos = [0, 0]

    for i in dat:
        key = i[:1]
        val = int(i[1:])
        
        if key == 'N':
            waypoint[1] = waypoint[1] + val
        elif key in 'S':
            waypoint[1] = waypoint[1] - val
        elif key == 'E':
            waypoint[0] = waypoint[0] + val
        elif key == 'W':
            waypoint[0] = waypoint[0] - val
        elif key == 'L':
            waypoint = turn(waypoint, LEFT, val)
        elif key == 'R':
            waypoint = turn(waypoint, RIGHT, val)
        else:
            pos = [pos[0] + val * waypoint[0], pos[1] + val * waypoint[1]]
    
    return pos
        


def turn(waypoint, dir, degrees):
    starting_waypoint = waypoint

    turns = degrees/90

    swap = turns % 2
    
    multiplier = [
        -1 * (int(math.sin(turns * math.pi / 2)) - int(math.cos(turns * math.pi / 2))),
        int(math.sin(turns * math.pi / 2)) + int(math.cos(turns * math.pi / 2))
    ]

    multiplier = [multiplier[0 + dir], multiplier[1 + dir]]

    waypoint = [waypoint[0] * multiplier[0], waypoint[1] * multiplier[1]]

    waypoint = [waypoint[0 - swap], waypoint[1 - swap]]

    return waypoint


if __name__ == '__main__':
    main()