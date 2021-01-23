import sys

def decode_pict(pict):
    if pict == '☒':
        return -1
    else:
        return 0

def encode_pict(char):
    if char == -1:
        return '☒'
    elif char == -2:
        return '☺'
    elif char == -3:
        return '☼'
    else:
        return '.'

func = open(sys.argv[1], 'r', encoding='utf-8')
map = []
line = func.readline()
x, y, xstart, ystart, xend, yend = 0, 0, 0, 0, 0, 0

while line:
    x = 0
    line_arr = []
    for c in line:
        if c != '\n':
            if c == '☺':
                xstart, ystart = x, y
            elif c == '☼':
                xend, yend = x, y
            line_arr.append(decode_pict(c))
            x += 1
    map.append(line_arr)
    line = func.readline()
    y += 1

w, h = x, y

def level(x, y, zn, map):
    map[y][x] = zn
    if y + 1 < h:
        if (map[y + 1][x] == 0) or (map[y + 1][x] != -1 and map[y + 1][x] > zn):
            level(x, y + 1, zn + 1, map)
    if x + 1 < w:
        if (map[y][x + 1] == 0) or (map[y][x + 1] != -1 and map[y][x + 1] > zn):
            level(x + 1, y, zn + 1, map)
    if x - 1 >= 0:
        if (map[y][x - 1] == 0) or (map[y][x - 1] != -1 and map[y][x - 1] > zn):
            level(x - 1, y, zn + 1, map)
    if y - 1 >= 0:
        if (map[y - 1][x] == 0) or (map[y - 1][x] != -1 and map[y - 1][x] > zn):
            level(x, y - 1, zn + 1, map)
    return map


def rewind(map):
    if map[yend][xend] != 0:
        x, y = xend, yend
        while (x, y) != (xstart, ystart):
            xprev, yprev = x, y
            if map[y + 1][x - 1] + 1 == map[y][x]:
                y += 1
                x -= 1
            elif map[y + 1][x] + 1 == map[y][x]:
                y += 1
            elif map[y + 1][x + 1] + 1 == map[y][x]:
                x += 1
                y += 1
            elif map[y][x - 1] + 1 == map[y][x]:
                x -= 1
            elif map[y][x + 1] + 1 == map[y][x]:
                x += 1
            elif map[y - 1][x - 1] + 1 == map[y][x]:
                x -= 1
                y -= 1
            elif map[y - 1][x] + 1 == map[y][x]:
                y -= 1
            elif map[y - 1][x + 1] + 1 == map[y][x]:
                x += 1
                y -= 1
            map[yprev][xprev] = -2
        map[y][x] = -2
    else:
        map[ystart][xstart] = -2
    return map


level(xstart, ystart, 1, map)

rewind(map)
map[yend][xend] = -3

for line in map:
    for i in line:
        print(encode_pict(i), end='')
    print()

func.close()
