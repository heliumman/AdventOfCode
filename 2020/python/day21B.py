import common
import day21A

def main():
    dat = common.readFile('day21.dat')
    
    #print(dat)
    parsed = day21A.parse_data(dat)
    mapping = {}

    done = False
    start_i = 0
    while not done:
        parsed, mapping, done, start_i = day21A.accumulate(parsed, mapping, start_i)
        print(mapping)
    
    sorted_keys = mapping.keys()
    sorted_keys.sort()
    print(sorted_keys)

    val = []
    for k in sorted_keys:
        val.append(mapping[k])
    
    print(','.join(val))

if __name__ == '__main__':
    main()