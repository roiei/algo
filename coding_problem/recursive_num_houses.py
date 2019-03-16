
street = [
0, 1, 1, 0, 1, 0, 0,
0, 1, 1, 0, 1, 0, 1,
1, 1, 1, 0, 1, 0, 1,
0, 0, 0, 0, 1, 1, 1,
0, 1, 0, 0, 0, 0, 0,
0, 1, 1, 1, 1, 1, 0,
0, 1, 1, 1, 0, 0, 0,
]
n = 7

def get_start_coord(street, n):
    for y in range(n):
        for x in range(n):
            if 1 == street[y*n + x]:
                return y, x
    return -1, -1

def count_num_houses(street, y, x, n):
    if 0 == street[y*n + x]:
        return 0
    num = 0
    if 1 == street[y*n + x]:
        street[y*n + x] = 0
        num += 1
    if y > 0:
        num += count_num_houses(street, y-1, x, n)
    if y < n-1:
        num += count_num_houses(street, y+1, x, n)
    if x > 0:
        num += count_num_houses(street, y, x-1, n)
    if x < n-1:
        num += count_num_houses(street, y, x+1, n)
    return num

# n = int(input())
# street = []
# for i in range(n):
#     street += list(map(int, input()))

sy = sy = 0
groups = []
while True:
    sy, sx = get_start_coord(street, n)
    print('sy = {}, sx = {}'.format(sy, sx))
    if -1 == sy:
        break
    groups.append(count_num_houses(street, sy, sx, n))

groups.sort()
print(len(groups))
for group in groups:
    print(group)

