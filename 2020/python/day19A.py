import common


def main():
    dat = common.readFile('day19.dat')
    
    print(dat)
    rules, words = parse_data(dat)
    print(rules)
    print(words)

    count = 0
    for word in words:
        print(word)
        valid, letter_id = apply_rule(word, rules, 0, 0)
        print(valid)
        if valid:
            count = count + 1
    
    print(count)



def apply_rule(word, rules, rule_id, letter_id):
    if type(rules[rule_id]) == type(''):
        if rules[rule_id] == list(word)[letter_id]:
            return (True, letter_id + 1)
        else:
            return (False, letter_id + 1)
    else:
        for rs in rules[rule_id]:
            valid = True
            tmp_letter_id = letter_id
            for r in rs:
                tmp, tmp_letter_id = apply_rule(word, rules, r, tmp_letter_id)
                valid = valid and tmp
            if rule_id == 0 and valid and tmp_letter_id < len(word):
                valid = False

            if valid:    
                letter_id = tmp_letter_id
                return (True, letter_id)
        
        return (False, letter_id)



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