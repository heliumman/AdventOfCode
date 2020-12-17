import common

def main():
    dat = common.readFile('day8.dat')

    steps = parse_dat(dat)
    print(find_loop(steps))

def parse_dat(dat):
    steps = []
    for step in dat:
        steps.append({'op': step.split(' ')[0].strip(), 'val': int(step.split(' ')[1].strip())})
    
    return steps

def find_loop(steps):
    steps_run = []
    accumulator = 0
    found_loop = False
    finished = False
    index = 0
    while not found_loop and not finished:
        if index >= len(steps):
            finished = True
        else:
            instruction = steps[index]['op']
            value = steps[index]['val']

            if index in steps_run:
                found_loop = True
                return accumulator
            else:
                steps_run.append(index)

                if instruction == 'jmp':
                    index = index + value
                else:
                    index = index + 1
                    if instruction == 'acc':
                        accumulator = accumulator + value

if __name__ == '__main__':
    main()