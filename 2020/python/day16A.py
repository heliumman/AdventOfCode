import common


def main() :
    dat = common.readFile('day16.dat')

    groups, my_ticket, nearby_tickets = split_info(dat)
    print(check_tickets(nearby_tickets, groups))

def check_tickets(tickets, groups):
    total = 0

    for t in tickets:
        for v in t:
            valid = 0
            for g in groups:
                if v in range(g[0][0], g[0][1] + 1) or v in range(g[1][0], g[1][1] + 1):
                    valid = valid + 1
            if valid == 0:
                total = total + v
    return total


def split_info(dat):
    groups = []
    my_ticket = []
    nearby_tickets = []

    category = 0

    for d in dat:
        if d == '':
            category = category + 1
        else:
            if category == 0:
                ranges = d.split(': ')[1].strip()
                cat = []
                for r in ranges.split(' or '):
                    cat.append((int(r.split('-')[0]), int(r.split('-')[1])))
                groups.append(cat)


            elif category == 1:
                if not d == 'your ticket:':
                    for i in d.split(','):
                        my_ticket.append(int(i))
            elif category == 2:
                if not d == 'nearby tickets:':
                    tmp = []
                    for i in d.split(','):
                        tmp.append(int(i))
                    nearby_tickets.append(tmp)
    
    return (groups, my_ticket, nearby_tickets)



if __name__ == '__main__':
    main()