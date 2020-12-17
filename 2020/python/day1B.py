import common

def main():
    dat = common.readFile('day1.dat')
    
    val = find_pair(dat)
    print(val[0]*val[1]*val[2])


def find_pair(input):
    found = False
    i = 0
    val = (0, 0, 0)

    while (not found and i < len(input)):
        j = i + 1
        while (not found and j < len(input)):
            k = j + 1
            while (not found and k < len(input)):
                found = (int(input[i]) + int(input[j]) + int(input[k])) == 2020
                if found:
                    val = (int(input[i]), int(input[j]), int(input[k]))
                
                k = k + 1
                
            j = j + 1
        
        i = i + 1
    
    return val


if __name__ == '__main__':
    main()