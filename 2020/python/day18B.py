import common


def main() :
    dat = common.readFile('day18.dat')
    
    answers = []
    for eq in dat:
        answers.append(mafs(eq))
    
    total = 0
    for a in answers:
        total = total + int(a)
    print(total)

def mafs(eq):
    tmp = ''
    sub_eq = ''
    sub_eq_pos= (0, 0)
    bracket_count = 0

    i = 0
    for l in list(eq):
        if bracket_count > 0:
            sub_eq = sub_eq + l
        else:
            if l != '(':
                tmp = tmp + l
        
        if l == '(':
            if bracket_count == 0:
                sub_eq_pos = (i, sub_eq_pos[1])
            bracket_count = bracket_count + 1
        
        if l == ')':
            bracket_count = bracket_count - 1
            if bracket_count == 0:
                sub_eq_pos = (sub_eq_pos[0], i)
                sub_eq = sub_eq[:-1]
                tmp = tmp +  str(mafs(sub_eq))
                sub_eq = ''
        
        i = i + 1

    tmps = tmp.split(' ')

    new_eq = []
    i = 0
    while i < len(tmps):
        if not tmps[i] == '+':
            new_eq.append(tmps[i])
        else:
            new_eq[-1] = str(int(new_eq[-1]) + int(tmps[i + 1]))
            i = i + 1
        i = i + 1
    tmps = []
    tmps.extend(new_eq)
    
    new_eq = []
    i = 0
    while i < len(tmps):
        if not tmps[i] == '*':
            new_eq.append(tmps[i])
        else:
            new_eq[-1] = str(int(new_eq[-1]) * int(tmps[i + 1]))
            i = i + 1
        i = i + 1
    tmps = []
    tmps.extend(new_eq)

    return tmps[0]

if __name__ == '__main__':
    main()