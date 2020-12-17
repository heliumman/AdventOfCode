import common
import day6A

def main():
    dat = common.readFile('day6.dat')

    groups = day6A.parse_dat(dat)
    
    print(group_intersection(groups))


def group_intersection(groups):
    total = 0
    for group in groups:
        group_set = set(list(group[0]))
        for i in group:
            group_set = group_set.intersection(set(list(i)))
        
        group_count = len(group_set)

        total = total + group_count
    
    return total


if __name__ == '__main__':
    main()