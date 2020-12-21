import common


def main():
    dat = common.readFile('day21.dat')
    
    #print(dat)
    parsed = parse_data(dat)
    mapping = {}

    done = False
    start_i = 0
    while not done:
        parsed, mapping, done, start_i = accumulate(parsed, mapping, start_i)
        print(mapping)
    
    print(count_remaining(parsed))

def count_remaining(parsed):
    total = 0
    for p in parsed:
        total = total + len(p[0])
    return total

def accumulate(parsed, mapping, start_i):
    i = start_i
    start_i = -1
    while i < len(parsed) and start_i == -1:
        if len(parsed[i][1]) > 0:
            start_i = i
        i = i + 1
    
    if start_i != -1:
        allergen_accum = parsed[start_i][1]
        ingred_accum = parsed[start_i][0]
        
        if len(ingred_accum) == 1:
            mapping[list(allergen_accum)[0]] = list(ingred_accum)[0]
            parsed = remove_ingred(parsed, list(ingred_accum)[0], list(allergen_accum)[0])
            return (parsed, mapping, False, 0)


        i = start_i + 1
        found = False

        while i < len(parsed) and not found:
            if len(allergen_accum.intersection(parsed[i][1])) > 0:
                allergen_accum = allergen_accum.intersection(parsed[i][1])
                ingred_accum = ingred_accum.intersection(parsed[i][0])
                if len(ingred_accum) == 1:
                    mapping[list(allergen_accum)[0]] = list(ingred_accum)[0]
                    parsed = remove_ingred(parsed, list(ingred_accum)[0], list(allergen_accum)[0])
                    found = True
            i = i + 1
        if found:
            return (parsed, mapping, False, 0)
        else:
            return (parsed, mapping, False, start_i + 1)
    else:
        return (parsed, mapping, True, 0)


def parse_data(dat):
    parsed = []
    for d in dat:
        ingred = set(d.split('(')[0].strip().split(' '))
        alergens = set(d.split('(contains')[1].strip().split(')')[0].split(', '))
        parsed.append((ingred, alergens))

    return parsed

def remove_ingred(parsed, ingred, allergen):
    tmp = []
    for p in parsed:
        try:
            p[0].remove(ingred)
            p[1].remove(allergen)
        except:
            pass
        
        tmp.append(p)
    return tmp

if __name__ == '__main__':
    main()