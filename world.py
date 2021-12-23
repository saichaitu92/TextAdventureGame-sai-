
_world = {}
starting_position = (0, 0)


def load_tiles(level):
    """Parses a file that describes the world space into the _world object"""

    if level == 0:
        with open('map.txt', 'r') as f:    # for difficulty level easy
            rows = f.readlines()
    elif level == 1:
        with open('map2.txt', 'r') as f:    # for difficulty level Medium
            rows = f.readlines()
    elif level == 2:
        with open('map3.txt', 'r') as f:     # for difficulty level hard
            rows = f.readlines()
    else:
        print("unidentified value given please select 0,1,2 ")
        exit()

    x_max = len(rows[0].split('|'))  # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('|')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
            if tile_name == 'StartRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))
