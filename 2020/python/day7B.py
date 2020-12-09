import common
import day7A

def main():
    dat = common.readFile('day7.dat')
    bag_dict = day7A.parse_dat(dat)
    print(get_child_count(bag_dict, 'shiny gold') - 1)

    
def get_child_count(bag_dict, colour):
    if len(bag_dict[colour]['children']) == 0:
        return 1
    else:
        children_count = 1
        for child in bag_dict[colour]['children']:
            children_count = children_count + int(child['count']) * get_child_count(bag_dict, child['name'])
        return children_count


if __name__ == '__main__':
    main()