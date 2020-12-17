import common

def main():
    dat = common.readFile('day4.dat')
    
    parsed = parse_data(dat)
    filtered = filter_objs(parsed)
    print(len(filtered))

def parse_data(dat):
    i = 0
    valid_count = 0
    temp_list = []
    objs = []
    for i in range(len(dat)):
        if dat[i] != '':
            temp_list.append(dat[i])
        else:
            str_obj = ' '.join(temp_list)
            temp_list = []
            obj = {}
            _str_obj = str_obj.split(' ')
            for kv in _str_obj:
                obj[kv.split(':')[0]] = kv.split(':')[1]
            objs.append(obj)
    if len(temp_list) > 0:
        str_obj = ' '.join(temp_list)
        temp_list = []
        obj = {}
        _str_obj = str_obj.split(' ')
        for kv in _str_obj:
            obj[kv.split(':')[0]] = kv.split(':')[1]
        objs.append(obj)
    
    return objs


def filter_objs(objs):
    required_keys = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'#,
        #'cid'
    ])
    filtered = []

    for obj in objs:
        if required_keys.issubset(set(obj.keys())):
            filtered.append(obj)
    
    return filtered



if __name__ == '__main__':
    main()