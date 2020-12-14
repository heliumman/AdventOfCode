import common


def main() :
    dat = common.readFile('day14.dat')
    parsed_dat = parse_input(dat)
    mem = process_dat(parsed_dat)
    print(sum_mem(mem))

def sum_mem(mem):
    total = 0
    for k in mem.keys():
        total = total + mem[k]
    
    return total

def process_dat(dat):
    vals = {}
    for mask in dat:
        for val in mask[1]:
            vals[val[0]] = mask_val(mask[0], convert_to_bin(val[1]))
    return vals

def parse_input(dat):
    input = []
    for d in dat:
        if d.startswith('mask'):
            input.append((d.split('= ')[1], []))
        else:
            key = int(d.split('[')[1].split(']')[0])
            val = int(d.split('= ')[1])
            input[-1][1].append((key, val))
    
    return input

def mask_val(mask, val):
    masked = ''
    i = 0
    while i < len(mask):
        if list(mask)[i] == 'X':
            masked = masked + list(val)[i]
        else:
            masked = masked + list(mask)[i]
        i = i + 1
    
    return int(masked, 2)



def convert_to_bin(i):
    return '{0:#038b}'.format(i)[2:]


if __name__ == '__main__':
    main()