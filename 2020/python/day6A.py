import common

def main():
    dat = common.readFile('day6.dat')

    groups = parse_dat(dat)
    
    print(group_union(groups))

def parse_dat(dat):
    temp_list = []
    groups = []
    for i in range(len(dat)):
        if dat[i] != '':
            temp_list.append(dat[i])
        else:
            groups.append(temp_list)
            temp_list = []
    if len(temp_list) > 0:
        groups.append(temp_list)
    
    return groups

def group_union(groups):
    total = 0
    for group in groups:
        group_set = set(list(group[0]))
        for i in group:
            group_set = group_set.union(set(list(i)))
        
        group_count = len(group_set)

        total = total + group_count
    
    return total


if __name__ == '__main__':
    main()