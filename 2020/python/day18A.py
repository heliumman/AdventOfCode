import common


def main() :
    dat = common.readFile('day18.dat')
    answers = []
    
    for eq in dat:
        answers.append(mafs(eq))
    
    total = 0
    for a in answers:
        total = total + a
    print(total)

def mafs(eq):
    #print('>' + eq + '<')
    total = 0
    sub_eq = ''
    bracket_count = 0

    MULTIPLY = 0
    ADD = 1

    op = ADD

    for p in eq.split(' '):
        
        if bracket_count == 0:
            if '(' in list(p):
                bracket_count = bracket_count + p.count('(')
            
                p = p[1:]
                sub_eq = p
            
            else:

                if p not in ['+', '*']:
                    if op == ADD:
                        total = total + int(p)
                    else:
                        total = total * int(p)
                else:
                    if p == '+':
                        op = ADD
                    else:
                        op = MULTIPLY
        
        else:
            sub_eq = (sub_eq + ' ' + p).strip()
            if '(' in list(p):
                bracket_count = bracket_count + p.count('(')

        if ')' in list(p):
            bracket_count = bracket_count - p.count(')')
            if bracket_count == 0:
                sub_eq = sub_eq[:-1]
                if op == ADD:
                    total = total + mafs(sub_eq)
                else:
                    total = total * mafs(sub_eq)

    
    return total


if __name__ == '__main__':
    main()