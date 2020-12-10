import common

def main() :
    dat = common.readFile('day10.dat')
    
    i = 0
    while i < len(dat):
        dat[i] = int(dat[i])
        i = i + 1
    
    sorted_dat = quicksort(dat[len(dat) - 1], dat)
    sorted_dat.insert(0, 0)
    sorted_dat.append(sorted_dat[-1] + 3)
    print(count_jolt_diffs(sorted_dat))


def quicksort(pivot, dat):
    
    pi = dat.index(pivot)
    i = 0
    max_index = len(dat)
    while i < max_index:
        if dat[i] <= pivot and pi < i:
            tmp = dat[i]
            dat.remove(tmp)
            dat.insert(pi, tmp)
            pi = pi + 1
        if dat[i] > pivot and pi > i:
            tmp = dat[i]
            dat.remove(tmp)
            dat.insert(pi, tmp)
            pi = pi - 1
            i = i - 1
            max_index = max_index - 1

        i = i + 1

    lower_split = dat[:pi]
    upper_split = dat[pi + 1:]

    if len(lower_split) > 0:
        lower_split = quicksort(lower_split[len(lower_split) - 1], lower_split)
    if len(upper_split) > 0:
        upper_split = quicksort(upper_split[len(upper_split) - 1], upper_split)

    sorted_dat = []
    sorted_dat.extend(lower_split)
    sorted_dat.append(pivot)
    sorted_dat.extend(upper_split)


    return sorted_dat


def count_jolt_diffs(dat):
    i = 0
    count1 = 0
    count3 = 0

    while i < len(dat) - 1:
        if dat[i + 1] - dat[i] == 1:
            count1 = count1 + 1
        if dat[i + 1] - dat[i] == 3:
            count3 = count3 + 1
        i = i + 1

    print(count1)
    print(count3)

    return count1 * count3


if __name__ == '__main__':
    main()