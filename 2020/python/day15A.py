import common


def main() :
    dat = common.readFile('day15.dat')
    nums = []
    last_seen = {}
    
    for d in dat[0].split(','):
        nums.append(int(d))
        last_seen[int(d)] = (dat[0].split(',').index(d) + 1, -1)
    
    nums = play_game(nums, last_seen)

    print(nums[-1])

def play_game(nums, last_seen):
    while len(nums) < 2020:
        last_num = nums[-1]
        last_said  = last_seen.get(last_num, (-1, -1))

        last_seen[last_num] = (len(nums), last_said[0])
        if last_seen[last_num][1] == -1:
            nums.append(0)
        else:
            nums.append(last_seen[last_num][0] - last_seen[last_num][1])
    
    return nums

if __name__ == '__main__':
    main()