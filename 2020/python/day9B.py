import common
import day9A

def main() :
    dat = common.readFile('day9.dat')
    consecutive_numbers = find_consecutive_numbers(dat, day9A.find_bad_number(dat))
    max_and_min = find_max_and_min(consecutive_numbers)

    print(max_and_min['max'] + max_and_min['min'])

def find_consecutive_numbers(numbers, target):
    target_index = numbers.index(target)
    
    i = 0
    consecutive_numbers = []
    found_consecutive_numbers = False

    while not found_consecutive_numbers and i < target_index:
        consecutive_numbers.append(numbers[i])
        running_total = sum_nums_in_list(consecutive_numbers)
        
        if running_total > int(target):
            consecutive_numbers = cull_consecutive_numbers(consecutive_numbers, target)
            running_total = sum_nums_in_list(consecutive_numbers)
        
        if running_total == int(target):
            found_consecutive_numbers = True
        
        i = i + 1
    
    return consecutive_numbers


def cull_consecutive_numbers(consecutive_numbers, target):
    while sum_nums_in_list(consecutive_numbers) > int(target):
        del consecutive_numbers[0]
    
    return consecutive_numbers


def sum_nums_in_list(numbers):
    total = 0
    for i in numbers :
        total = total + int(i)
    
    return total

def find_max_and_min(numbers):
    max_number = int(numbers[0])
    min_number = int(numbers[0])

    for i in numbers:
        max_number = max(max_number, int(i))
        min_number = min(min_number, int(i))
    
    return {'max': max_number, 'min': min_number}


if __name__ == '__main__':
    main()