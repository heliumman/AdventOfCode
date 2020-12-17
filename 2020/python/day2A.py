import common

def main():
    dat = common.readFile('day2.dat')
    
    parsed = parse_data(dat)
    print(count_valid(parsed))

def parse_data(dat):
    parsed = []

    for i in dat:
        i_ = i.split(' ')
        
        min_pos = int(i_[0].split('-')[0])
        max_pos = int(i_[0].split('-')[1])
        char = i_[1].split(':')[0]
        password = i_[2]

        parsed.append((min_pos, max_pos, char, password))
    
    return parsed

def count_valid(dat):
    valid_count = 0
    
    for d in dat:
        tmp = 0
        
        for l in list(d[3]):
            if l == d[2]:
                tmp = tmp + 1
        
        if tmp >= d[0] and tmp <= d[1]:
            valid_count = valid_count + 1

    return valid_count

if __name__ == '__main__':
    main()