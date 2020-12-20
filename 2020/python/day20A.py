import common


def main():
    dat = common.readFile('day20.dat')
    dat.append('')
    tiles = parse_data(dat)
    total, tiles = find_image(tiles)
    print(total)    

def parse_data(dat):
    tiles = {}

    tile = []
    for d in dat:
        if d.startswith('Tile'):
            tile_id = int(d.split('Tile ')[1].split(':')[0].strip())
        elif d == '':
            tiles[tile_id] = tile
            tile = []
        else:
            tile.append(list(d))

    return tiles

def tile_variations(tile):
    tiles = [tile]

    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))

    new_tile = []
    for t in tile:
        new_tile.insert(0, t)
    
    tiles.append(new_tile)

    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))

    new_tile = []
    for t in tile:
        tmp = []
        for p in t:
            tmp.insert(0, p)
        new_tile.append(tmp)
    
    tiles.append(new_tile)

    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))
    tiles.append(rotate_tile(tiles[-1]))

    return tiles

def rotate_tile(tile):
    new_tile = []
    
    j = 0
    while j < len(tile):
        i = len(tile) - 1
        tmp = []
        while i >= 0:
            tmp.append(tile[i][j])
            i = i - 1
        new_tile.append(tmp)
        j = j + 1
    
    return new_tile

def find_image(tiles):
    dim = int(pow(len(tiles), .5))
    for k in tiles.keys():
        res = try_tile(tiles, k)
        if res:
            res, tiles = res
            total = res[0][0] * res[0][dim - 1] * res[dim - 1][0] * res[dim - 1][dim - 1]
            return total, tiles
    

def try_tile(tiles, id):
    dim = int(pow(len(tiles), .5))

    ids = []
    ts = []

    for var in tile_variations(tiles[id]):

        ids = []
        ts = []

        tmp_tiles = {}
        for k in tiles.keys():
            if not k == id:
                tmp_tiles[k] = tiles[k]

        i = 0
        while i < dim:
            ts.append([])   
            ids.append([])

            j = 0
            while j < dim:
                above = None
                left = None
                if i == 0 and j == 0:
                    ids[-1].append(id)
                    ts[-1].append(var)

                else:
                    if i > 0:
                        above = ts[i - 1][j]
                    if j > 0:
                        left = ts[i][j - 1]

                    k = 0
                    found = False
                    while k < len(tmp_tiles.keys()) and not found:
                        fit = test_fit(above, left, tmp_tiles[tmp_tiles.keys()[k]])
                        if fit:
                            ids[-1].append(tmp_tiles.keys()[k])
                            ts[-1].append(fit)
                            del tmp_tiles[tmp_tiles.keys()[k]]
                            found = True
                        k = k + 1
                    if not found:
                        j = dim
                        i = dim
                j = j + 1
            i = i + 1
        if (i, j) == (dim, dim):
            return (ids, ts)


def test_fit(above, left, tile):
    for var in tile_variations(tile):
        fits = True
        
        if above:
            fits = fits and above[-1] == var[0]
        
        if left:
            i = 0
            tmp = ''
            tmp2 = ''
            while i < len(tile):
                tmp = tmp + left[i][-1]
                tmp2 = tmp2 + var[i][0]
                i = i + 1
            fits = fits and tmp == tmp2
    
        if fits:
            return var
    
    return None


if __name__ == '__main__':
    main()