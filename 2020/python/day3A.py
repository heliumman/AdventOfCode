import common

def main():
    dat = common.readFile('day3.dat')
    
    print(toboggan(dat))

def toboggan(dat):
    pos = 0
    tree_count = 0
    i = 1

    while i < len(dat):
        row = list(dat[i])
        
        pos = (pos + 3) % len(row)
        
        if row[pos] == '#':
            tree_count = tree_count + 1

        i = i + 1

    return tree_count


if __name__ == '__main__':
    main()