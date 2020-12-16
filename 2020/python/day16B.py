import common


def main() :
    dat = common.readFile('day16.dat')

    groups, group_names, my_ticket, nearby_tickets = split_info(dat)
    nearby_tickets.append(my_ticket)

    combinations = check_tickets(nearby_tickets, groups)
    common_groups = find_common_groups(combinations)
    group_dict = find_final_group(common_groups, group_names)

    total = 1
    for k in group_dict.keys():
        if k.startswith('departure'):
            total = total * my_ticket[group_dict[k]]
    
    print(total)



def find_common_groups(combinations):
    running_total = combinations[0]
    for c in combinations:
        for s in c:
            running_total[c.index(s)] = running_total[c.index(s)].intersection(s)
    
    return running_total

def find_final_group(groups, group_names):
    for g in groups:
        groups[groups.index(g)] = list(g)
    
    group_dict = {}

    counter = 0

    while counter < len(groups):

        group_to_remove = -1
        i = 0

        while i < len(groups) and group_to_remove == -1:
            if type(groups[i]) == type([]):
                if len(groups[i]) == 1:
                    groups[i] = groups[i][0]
                    group_dict[group_names[groups[i]]] = i
                    group_to_remove = groups[i]
                    counter = counter + 1
            i = i + 1
        
        if not group_to_remove == -1:
            j = 0
            while j < len(groups):
                if type(groups[j]) == type([]):
                    groups[j].remove(group_to_remove)
                j = j + 1
    
    return group_dict


def check_tickets(tickets, groups):
    combinations = []

    for t in tickets:
        tmp = []
        for v in t:
            valid = []
            for g in groups:
                if v in range(g[0][0], g[0][1] + 1) or v in range(g[1][0], g[1][1] + 1):
                    valid.append(groups.index(g))
            if len(valid) > 0:
                tmp.append(set(valid))
        if len(tmp) == len(t):
            combinations.append(tmp)
    return combinations


def split_info(dat):
    groups = []
    group_names = []
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
                group_names.append(d.split(': ')[0].strip())


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
    
    return (groups, group_names, my_ticket, nearby_tickets)



if __name__ == '__main__':
    main()