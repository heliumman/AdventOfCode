import common
import day10A
from itertools import combinations 

def main() :
    dat = common.readFile('day10.dat')
    
    i = 0
    while i < len(dat):
        dat[i] = int(dat[i])
        i = i + 1

    sorted_dat = day10A.quicksort(dat[0], dat)
    sorted_dat.insert(0, 0)
    sorted_dat.append(sorted_dat[-1] + 3)

    sets = group_sets(sorted_dat)
    set_combs = set_combinations(sets)


    print(count_combinations(sets, set_combs))
    #print(valid_set(sorted_dat))


def group_sets(dat):
    sets = {}

    i = 0
    tmp = 1
    while i < len(dat) - 1:
        if dat[i + 1] - dat[i] == 1:
            tmp = tmp + 1
        else:
            if tmp > 2:
                count = sets.get(tmp, 0)
                sets[tmp] = count + 1
            tmp = 1
        i = i + 1

    return sets


def set_combinations(sets):
    combs = {}
    for k in sets.keys():
        set_ = list(range(k))
        valid_sets = []
        #print(set_)
        for i in range(k-1):
            comb = combinations(set_[1:-1], i)
            for c in list(comb):
                tmp_set = []
                tmp_set.extend(set_)
                for v in c:
                    tmp_set.remove(v)
                if valid_set(tmp_set):
                    valid_sets.append(tmp_set)
        combs[k] = valid_sets
        #print(valid_sets)
    return combs


def valid_set(dat):
    i = 0
    valid_set = True

    while i < len(dat) - 1 and valid_set:
        if dat[i + 1] - dat[i] > 3:
            valid_set = False
        i = i + 1

    return valid_set


def count_combinations(sets, set_combs):
    count = 1
    for k in sets.keys():
        count = count * pow(len(set_combs[k]), sets[k])
    
    return count


if __name__ == '__main__':
    main()