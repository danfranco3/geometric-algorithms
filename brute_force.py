
def p_in_r(p: [tuple], r: [tuple]):
    if (p[0] >= r[0]) and (p[0] <= r[1]) and (p[1] >= r[2]) and (p[1] <= r[3]):
        return True
    return False


n_points_str = input()
_lst = n_points_str.split()
n_points = int(_lst[1])

points_list = []

for _ in range(0, n_points):
    _cur = input()
    _x, _y = _cur.split()
    points_list.append((int(_x), int(_y)))

n_rectangles_str = input()
_lst = n_rectangles_str.split(" ")
n_rectangles = int(_lst[1])

rectangles_list = []

for _ in range(0, n_rectangles):
    _cur = input()
    _w, _x, _y, _z = _cur.split()
    rectangles_list.append((int(_w), int(_x), int(_y), int(_z)))

result = 0

for _p in points_list:
    for _r in rectangles_list:
        if p_in_r(_p, _r):
            result += 1

print(result)
