import common

FLOOR = 0
EMPTY = 1
OCCUPIED = 2

def main() :
    dat = common.readFile('day11.dat')

    seats = parse_input(dat)

    final_seats = find_equilibrium(seats)
    print(count_occupied_seats(final_seats))
    

def parse_input(dat):
    seats = []

    for ln in dat:
        row = []
        for l in list(ln):
            if l == 'L':
                row.append(EMPTY)
            else:
                row.append(FLOOR)
        seats.append(row)
    
    return seats


def update_seats(seats):
    tmp_seats = []

    i = 0
    while i < len(seats):
        j = 0

        tmp_row = []
        while j < len(seats[0]):
            if seats[i][j] == EMPTY and count_adjacent(seats, j, i) == 0:
                tmp_row.append(OCCUPIED)
            elif seats[i][j] == OCCUPIED and count_adjacent(seats, j, i) >= 4:
                tmp_row.append(EMPTY)
            else:
                tmp_row.append(seats[i][j])

            j = j + 1

        tmp_seats.append(tmp_row)
        i = i + 1

    return tmp_seats


def count_occupied_seats(seats):
    occupied_seats = 0
    for row in seats:
        for s in row:
            if s == OCCUPIED:
                occupied_seats = occupied_seats + 1

    return occupied_seats


def find_equilibrium(seats):
    equilibrium = False

    tmp_seats = seats
    while not equilibrium:
        if tmp_seats == update_seats(tmp_seats):
            equilibrium = True
        else:
            tmp_seats = update_seats(tmp_seats)
    
    return tmp_seats


def count_adjacent(seats, posx, posy):
    max_seat = len(seats) - 1
    max_row = len(seats[0]) - 1

    adjacent_seats = 0
    if posy - 1 >= 0:
        if seats[posy - 1][posx] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posy - 1 >= 0 and posx + 1 <= max_row:
        if seats[posy - 1][posx + 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posx + 1 <= max_row:
        if seats[posy][posx + 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posy + 1 <= max_seat and posx + 1 <= max_row:
        if seats[posy + 1][posx + 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posy + 1 <= max_seat:
        if seats[posy + 1][posx] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posy + 1 <= max_seat and posx - 1 >= 0:
        if seats[posy + 1][posx - 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posx - 1 >= 0:
        if seats[posy][posx - 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1
    if posy - 1 >= 0 and posx - 1 >= 0:
        if seats[posy - 1][posx - 1] == OCCUPIED:
            adjacent_seats = adjacent_seats + 1

    return adjacent_seats

if __name__ == '__main__':
    main()