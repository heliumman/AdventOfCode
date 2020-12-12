import common

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

LEFT = -1
RIGHT = 1

def main() :
    dat = common.readFile('day12.dat')

    end_pos = travers_directions(dat)
    print(abs(end_pos[0]) + abs(end_pos[1]))


def travers_directions(dat):
    facing = EAST
    pos = [0, 0]

    for i in dat:
        key = i[:1]
        val = int(i[1:])
        
        if key == 'N':
            pos[0] = pos[0] + val
        elif key in 'S':
            pos[0] = pos[0] - val
        elif key == 'E':
            pos[1] = pos[1] + val
        elif key == 'W':
            pos[1] = pos[1] - val
        elif key == 'L':
            facing = turn(facing, LEFT, val)
        elif key == 'R':
            facing = turn(facing, RIGHT, val)
        else:
            if facing in [SOUTH, WEST]:
                val = val * -1
            pos[facing%2] = pos[facing%2] + val
    
    return pos
        


def turn(facing, dir, degrees):
    return (facing + (dir * degrees/90)) % 4


if __name__ == '__main__':
    main()