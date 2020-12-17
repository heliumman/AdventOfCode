import common

def main():
    dat = common.readFile('day3.dat')
    
    trees = toboggan(dat)

    total = 1
    for t in trees:
        total = total * t
    
    print(total)

def toboggan(dat):
    pos = [0, 0, 0, 0, 0]
    tree_count = [0, 0, 0, 0, 0]
    deltas = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    i = 1

    while i < len(dat):
        row = list(dat[i])
        
        for d in deltas:
            if i % d[1] == 0:
                pos[deltas.index(d)] = (pos[deltas.index(d)] + d[0]) % len(row)
        
                if row[pos[deltas.index(d)]] == '#':
                    tree_count[deltas.index(d)] = tree_count[deltas.index(d)] + 1

        i = i + 1

    return tree_count


if __name__ == '__main__':
    main()