import common
import day20A

def main():
    dat = common.readFile('day20.dat')
    dat.append('')
    tiles = day20A.parse_data(dat)
    total, tiles = day20A.find_image(tiles)
    
    joined = join_tiles(tiles)
    print(find_monster(joined))

def find_monster(joined):
    sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]

    joined_vars = day20A.tile_variations(joined)

    for v in joined_vars:

        results, count = search_image(v, sea_monster)
        if count > 0:
            hash_count = count_hashes(results)
            return hash_count

def count_hashes(image):
    count = 0
    for r in image:
        for l in r:
            if l == '#':
                count = count + 1
    
    return count

def search_image(image, sm):
    dim = (len(sm[0]), len(sm))
    count = 0

    j = 0
    while j < len(image[0]) - (dim[0] - 1):
        i = 0
        while i < len(image) - (dim[1] - 1):

            tmp = []
            l = 0
            while l < dim[1]:
                tmp.append(''.join(image[i + l][j:j + dim[0]]))
                l = l + 1

            if has_monster(tmp, sm):
                count = count + 1
                l = 0
                while l < dim[1]:
                    m = 0
                    while m < dim[0]:
                        
                        if list(sm[l])[m] == '#':
                            image[i + l][j + m] = 'O'

                        m = m + 1
                    l = l + 1

            i = i + 1
        j = j + 1

    return (image, count)

def has_monster(image, sm):
    hashes = 0
    matches = 0

    i = 0
    while i < len(image):
        j = 0
        while j < len(list(image[0])):

            if list(sm[i])[j] == '#':
                hashes = hashes + 1
                if list(image[i])[j] == '#':
                    matches = matches + 1

            j = j + 1
        i = i + 1
    
    return hashes == matches


def join_tiles(tiles):
    pic = []

    for ts in tiles:
        i = 1
        while i < len(tiles[0][0]) - 1:
            tmp = []
            for t in ts:
                j = 1
                while j < len(tiles[0][0]) - 1:
                    tmp.append(t[i][j])
                    j = j + 1
            i = i + 1
            pic.append(tmp)
    
    return pic

if __name__ == '__main__':
    main()