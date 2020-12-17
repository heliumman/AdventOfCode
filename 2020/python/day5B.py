import common
import day5A

def main():
    dat = common.readFile('day5.dat')

    seats = day5A.parse_dat(dat)
    print(cull_seats(seats))
    

def cull_seats(seats):
    all_seats = list(range(0b10000000000))

    for seat in seats:
        all_seats.remove(int(seat, 2))
    
    tmp = []
    tmp.extend(all_seats)

    i = 1

    while i < len(all_seats) - 1:
        if all_seats[i - 1] + 1 == all_seats[i] or all_seats[i + 1] - 1 == all_seats[i]:
            tmp.remove(all_seats[i])
        
        i = i + 1

    return tmp[1]


if __name__ == '__main__':
    main()