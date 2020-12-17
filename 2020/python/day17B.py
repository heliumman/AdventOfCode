import common


def main() :
    dat = common.readFile('day17.dat')
    pd, dims = parse_dat(dat)

    i = 0
    while i < 6:
        pd, dims = new_pd(pd, dims)
        i = i + 1
    
    print(count_active(pd))

def parse_dat(dat):
    pd = {}
    i = 0
    for d in dat:
        j = 0
        for l in list(d):
            pd[(j, i, 0, 0)] = l
            j = j + 1
        i = i + 1
    return (pd, ((0, len(pd)/abs(i)), (0, abs(i)), (0, 1), (0, 1)))

def check_neighbours(pd, x, y, z, w):
    count = 0
    
    for i in range(-1, 2):
        for j in range(-1,2):
            for k in range (-1, 2):
                for l in range (-1, 2):
                    if not (i, j, k, l) == (0,0,0, 0):
                        if pd.get((x + i, y + j, z + k, w + l), '.') == '#':
                            count = count + 1
    
    if pd.get((x,y,z, w), '.') == '.':
        if count == 3:
            return '#'
        else:
            return '.'
    else:
        if count in [2,3]:
            return '#'
        else:
            return '.'

def new_pd(pd, dims):
    pd_ = {}
    dims = (
        (dims[0][0] - 1, dims[0][1] + 1),
        (dims[1][0] - 1, dims[1][1] + 1),
        (dims[2][0] - 1, dims[2][1] + 1),
        (dims[3][0] - 1, dims[3][1] + 1)
    )

    for x in range(dims[0][0], dims[0][1]):
        for y in range(dims[1][0], dims[1][1]):
            for z in range(dims[2][0], dims[2][1]):
                for w in range(dims[3][0], dims[3][1]):
                    pd_[(x, y, z, w)] = check_neighbours(pd, x, y, z, w)
    
    return (pd_, dims)

def count_active(pd):
    count = 0
    for k in pd.keys():
        if pd[k] == '#':
            count = count + 1
    return count

def print_z(pd, dims, z):
    for y in range(dims[1][0], dims[1][1]):
        for x in range(dims[0][0], dims[0][1]):
            print(pd[(x,y,z)]),
        print

if __name__ == '__main__':
    main()