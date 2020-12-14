import common
import math


def main() :
    dat = common.readFile('day13.dat')
    time, busses = parse_input(dat)

    depart_time, bus = find_bus(time, busses)
    print((depart_time - time) * bus)


def parse_input(dat):
    time = int(dat[0])
    busses = []

    for i in dat[1].split(','):
        if not i == 'x':
            busses.append(int(i))
    
    return (time, busses)

def find_bus(time, busses):
    bus_id = 0
    min_time = 2*time

    for bus in busses:
        tmp_time = (int(time/bus) + 1) * bus
        if tmp_time < min_time:
            bus_id = bus
            min_time = tmp_time
    
    return (min_time, bus_id)



if __name__ == '__main__':
    main()