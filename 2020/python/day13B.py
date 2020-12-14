import common
import math


def main() :
    dat = common.readFile('day13.dat')
    busses = parse_input(dat)

    earliest_time = find_bus2(busses)
    print(earliest_time)


def parse_input(dat):
    busses = []

    ind = 0
    for i in dat[1].split(','):
        if not i == 'x':
            busses.append((int(i), ind))
        ind = ind + 1
    
    return busses


def find_bus2(busses):
    i = 1

    funcs = []

    while i < len(busses):
        funcs.append(lambda x, i : (float((x * busses[0][0] + busses[i][1])) / float(busses[i][0])).is_integer())
        i = i + 1


    found_earliest_time = False
    counter = 546156
    while not found_earliest_time:
        tmp = True
        for f in funcs:
            if f(counter, funcs.index(f) + 1):
                pass
            else:
                tmp = False
        found_earliest_time = tmp
        
        counter = counter + 546157

    return (counter - 546157) * busses[0][0]



def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def find_bus(busses):
    max_bus = max_index(busses)
    i = busses[max_bus] - max_bus
    delta = busses[max_bus]
    found_earliest_time = False

    val = 0
    while not found_earliest_time:
        j = 0
        tmp = True
        print(i)
        while j < len(busses):
            if not busses[j] == -1:
                if float(i + j)/float(busses[j]) == float((i + j)/int(busses[j])):
                    pass
                else:
                    tmp = False
            j = j + 1

        found_earliest_time = tmp
        val = i
        i = i + delta

    return val


def max_index(busses):
    i = 0
    max_bus = 0

    for bus in busses:
        if bus > max_bus:
            max_bus = bus
            i = busses.index(bus)

    return i


if __name__ == '__main__':
    main()