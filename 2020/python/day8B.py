import common
import day8A
import copy

def main():
    dat = common.readFile('day8.dat')

    steps = day8A.parse_dat(dat)
    print(fix_instructions(steps))

def check_instructions(steps):
    steps_run = []
    accumulator = 0
    found_loop = False
    finished = False
    index = 0
    while not found_loop and not finished:
        if index >= len(steps):
            finished = True
            return (True, accumulator)
        else:
            instruction = steps[index]['op']
            value = steps[index]['val']

            if index in steps_run:
                found_loop = True
                return (False, accumulator)
            else:
                steps_run.append(index)

                if instruction == 'jmp':
                    index = index + value
                else:
                    index = index + 1
                    if instruction == 'acc':
                        accumulator = accumulator + value


def fix_instructions(rules):
    
    i = 0
    finished = False
    accumulator = 0

    while i < len(rules) and not finished:
        
        temp_rules = copy.deepcopy(rules)
        if temp_rules[i]['op'] == 'jmp':
            temp_rules[i]['op'] = 'nop'
            finished, accumulator = check_instructions(temp_rules)
        elif temp_rules[i]['op'] == 'nop':
            temp_rules[i]['op'] = 'jmp'
            finished, accumulator = check_instructions(temp_rules)
        i = i + 1
    
    return accumulator

if __name__ == '__main__':
    main()