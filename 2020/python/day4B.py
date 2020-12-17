import common
import day4A
import re

def main():
    dat = common.readFile('day4.dat')
    
    parsed = day4A.parse_data(dat)
    filtered = day4A.filter_objs(parsed)
    filtered = regex_tests(filtered)
    print(len(filtered))


def regex_tests(objs):
    filtered = []

    for obj in objs:
        tmp = 0

        if re.search(r"^\d{4}$", obj['byr']) and int(obj['byr']) >= 1920 and int(obj['byr']) <= 2002:
            tmp = tmp + 1
        
        if re.search(r"^\d{4}$", obj['iyr']) and int(obj['iyr']) >= 2010 and int(obj['iyr']) <= 2020:
            tmp = tmp + 1
        
        if re.search(r"^\d{4}$", obj['eyr']) and int(obj['eyr']) >= 2020 and int(obj['eyr']) <= 2030:
            tmp = tmp + 1
        
        if re.search(r"^#[a-f0-9]{6}$", obj['hcl']):
            tmp = tmp + 1
        
        if obj['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            tmp = tmp + 1
        
        if re.search(r"^\d{9}$", obj['pid']):
            tmp = tmp + 1
        
        if obj['hgt'].endswith('in'):
            hgt_num = obj['hgt'].split('in')[0]
            if int(hgt_num) >= 59 and int(hgt_num) <= 76:
                tmp = tmp + 1
        if obj['hgt'].endswith('cm'):
            hgt_num = obj['hgt'].split('cm')[0]
            if int(hgt_num) >= 150 and int(hgt_num) <= 193:
                tmp = tmp + 1
        
        if tmp == 7:
            filtered.append(obj)


    return filtered


if __name__ == '__main__':
    main()