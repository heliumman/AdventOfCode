import common


def main() :
    dat = common.readFile('day9.dat')
    print(find_bad_number(dat))


def check_number(prev, number):
    
    i = 0

    valid_number = False

    while i < len(prev) - 1:
        j = i + 1
        while j < len(prev):
            if (int(prev[i]) + int(prev[j])) == int(number) :
                valid_number = True
            j = j + 1
        i = i + 1
    
    return not valid_number


def find_bad_number(numbers):
    
    found_bad_number = False
    prev = numbers[0:25]
    numbers_to_check = numbers[25:]
    bad_number = 0

    while not found_bad_number and len(numbers_to_check) > 0:
        num_to_check = numbers_to_check[0]
        found_bad_number = check_number(prev, num_to_check)
        if found_bad_number:
            bad_number = num_to_check


        del prev[0]
        prev.append(num_to_check)

        del numbers_to_check[0]
    
    return bad_number



if __name__ == '__main__':
    main()