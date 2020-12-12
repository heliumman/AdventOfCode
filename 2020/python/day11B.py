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
            elif seats[i][j] == OCCUPIED and count_adjacent(seats, j, i) >= 5:
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
        
        seats_to_check = update_seats(tmp_seats) 
        if tmp_seats == seats_to_check:
            equilibrium = True
        else:
            tmp_seats = seats_to_check
    
    return tmp_seats


def count_adjacent(seats, posx, posy):
    max_seat = len(seats) - 1
    max_row = len(seats[0]) - 1

    adjacent_seats = 0

    for i in range(3):
        for j in range(3):
            if not (i - 1 == 0 and j - 1 == 0):
                adjacent_seats = adjacent_seats + check_seat(seats, posx, posy, i - 1, j - 1)
    
    return adjacent_seats

def check_seat(seats, posx, posy, deltax, deltay):
    found_seat = False
    adjacent = 0

    offsetx = 0
    offsety = 0

    while not found_seat:
        offsetx = offsetx + deltax
        offsety = offsety + deltay

        if posx + offsetx == len(seats[0]) or posx + offsetx == -1:
            found_seat = True
        elif posy + offsety == len(seats) or posy + offsety == -1:
            found_seat = True
        else:
            if seats[posy + offsety][posx + offsetx] == OCCUPIED:
                found_seat = True
                adjacent = 1
            elif seats[posy + offsety][posx + offsetx] == EMPTY:
                found_seat = True

    return adjacent



if __name__ == '__main__':
    main()