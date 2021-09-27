import bisect

limits = []
test = []

N, M = 3, 3
limits += (50, 50),
limits += (40, 40),
limits += (10, 30),
test += (60, 76),
test += (18, 28),
test += (22, 50),


N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    limits += tuple(map(int, sys.stdin.readline().split())),

for i in range(M):
    test += tuple(map(int, sys.stdin.readline().split())),
    

# limits += (50, 90),
# limits += (10, 90),
# limits += (40, 50),
# test += (50, 40),
# test += (10, 100),
# test += (40, 40),


tbl = [(0, 0)]
start = 0

for length, speed in limits:
    tbl += (start + length, speed),
    start += length

valid = []
start = 0
for length, speed in test:
    valid += (start + 1, start + length, speed),
    start += length


def search(vals, target):
    l = 0
    r = len(vals) - 1

    while l <= r:
        m = (l + r)//2
        if vals[m][0] == target:
            return m

        if vals[m][0] < target:
            l = m + 1
        else:
            r = m - 1

    return l


mx = 0
for start, end, speed in valid:
    for target in [start, end]:
        idx = search(tbl, target)
        diff = speed - tbl[idx][1]
        print(diff)
        mx = max(mx, diff)

print('mx = ', mx)