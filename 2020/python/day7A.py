import common

def main():
    dat = common.readFile('day7.dat')
    bag_dict = parse_dat(dat)
    print(traverse_parents(bag_dict, 'shiny gold'))

def parse_dat(dat):
    rules = {}
    for rule in dat:
        name = rule.split('bags contain')[0].strip()
        rule_obj = rules.get(name, {'name': name, 'parents': [], 'children': []})

        children = []
        str_children = rule.split('bags contain')[1].split('.')[0].replace('bags', '').replace('bag', '').strip()
        str_children_ = str_children.split(', ')

        if rule.strip().endswith('contain no other bags.'):
            str_children_ = []

        for str_child in str_children_:
            child_count = str_child.split(' ', 1)[0]
            child_name = str_child.split(' ', 1)[1].replace('bags', '').replace('bag', '').strip()

            rule_obj['children'].append({'count': child_count, 'name': child_name})
            rules[name] = rule_obj

            child_obj = rules.get(child_name, {'name': child_name, 'parents': [], 'children': []})
            child_obj['parents'].append(name)
            rules[child_name] = child_obj
    
    return rules

def traverse_parents(bag_dict, starting_colour):
    parents = set(bag_dict[starting_colour]['parents'])
    traversed_set = set([])

    while len(parents) > 0:
        traversed_set = traversed_set.union(parents)

        temp_parents = set([])
        for parent in parents:
            temp_parents = temp_parents.union(bag_dict[parent]['parents'])
        parents = temp_parents.difference(traversed_set)

    return len(traversed_set)

if __name__ == '__main__':
    main()