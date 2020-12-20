import common


def main():
    dat = common.readFile('day19.dat')
    
    rules, words = parse_data(dat)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    count = 0
    for word in words:
        leftovers = apply_rule3(word, rules, 0)
        #print('' in leftovers, word)
        
        if '' in leftovers:
            count = count + 1
    
    print(count)
        

def apply_rule3(word, rules, rule_id):
    if type(rules[rule_id]) == type(''):
        if len(word) == 0:
            return []
        if rules[rule_id] == list(word)[0]:
            return [word[1:]]
        else:
            return []
    
    tmps = []
    for rs in rules[rule_id]:
        i = 0
        good = True

        tmp = []
        res = [word]
        while i < len(rs) and good:
            new_res = []
            
            for j in res:
                new_res.extend(apply_rule3(j, rules, rs[i]))
            
            res = []
            res.extend(new_res)

            i = i + 1

            if len(res) == 0:
                good = False
        if len(res) > 0:
            tmps.extend(res)

    return tmps

def parse_data(dat):
    rules = {}
    words = []

    section = 0

    for d in dat:
        if d == '':
            section = section + 1
        else:            
            if section == 0:
                key = int(d.split(':')[0].strip())
                val = d.split(':')[1].strip()

                if '"' in list(val):
                    rules[key] = val.replace('"', '').strip()
                
                else:
                    tmp = []
                    tmp2 = []
                    for l in val.split(' '):
                        if l == '|':
                            tmp.append(tmp2)
                            tmp2 = []
                        else:
                            tmp2.append(int(l))
                    tmp.append(tmp2)

                    rules[key] = tmp
                


            else:
                words.append(d)

    return (rules, words)


if __name__ == '__main__':
    main()