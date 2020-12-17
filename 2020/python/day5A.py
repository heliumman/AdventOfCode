import common

def main():
    dat = common.readFile('day5.dat')

    seats = parse_dat(dat)
    
    print(max_seat(seats))

def parse_dat(dat):
    seats = []

    for d in dat:
        seat = d.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        
        seats.append(seat)
    
    return seats

def max_seat(seats):
    max_seat_id = -1

    for seat in seats:
        seat_id = int(seat, 2)

        max_seat_id = max(max_seat_id, seat_id)
    
    return max_seat_id

if __name__ == '__main__':
    main()