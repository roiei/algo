import bisect

limits = []
test = []

N, M = 3, 3
limits += [50, 50],
limits += [40, 40],
limits += [10, 30],
test += (60, 76),
test += (18, 28),
test += (22, 50),


# N, M = map(int, sys.stdin.readline().split())

# for i in range(N):
#     limits += tuple(map(int, sys.stdin.readline().split())),

# for i in range(M):
#     test += tuple(map(int, sys.stdin.readline().split())),
    

# limits = []
# test = []
# limits += [50, 90],
# limits += [10, 90],
# limits += [40, 50],
# test += (50, 40),
# test += (10, 100),
# test += (40, 40),

#def impl3():

def get_points(intput_set):
    points = {}
    pos = 0
    for length, speed in intput_set:
        points[pos] = speed
        pos += length

    return points

limits = get_points(limits)
test = get_points(test)
points = sorted(set(set(limits.keys()) | set(test.keys())))
mx = 0
limit_speed = test_speed = 0

for point in points:
    if point in limits:
        limit_speed = limits[point]

    if point in test:
        test_speed = test[point]

    if test_speed > limit_speed:
        mx = max(mx, test_speed - limit_speed)

print(mx)





def impl2():
    for i in range(len(limits) - 1):
        limits[i + 1][0] += limits[i][0]

    for i in range(len(test) - 1):
        test[i + 1][0] += test[i][0]

    mx = 0
    for end, speed in test:
        while limits and limits[0][0] < end:
            if speed > limits[0][1]:
                mx = max(speed - limits[0][1], mx)
            limits.pop(0)

        if limits and end <= limits[0][0]:
            if speed > limits[0][1]:
                mx = max(speed - limits[0][1], mx)

        if limits and limits[0][0] == end:
            limits.pop(0)

    print(mx)







def impl1():
    tbl = [(0, 0)]
    start = 1

    for length, speed in limits:
        tbl += (start + length - 1, speed),
        start += length

    valid = []
    start = 1
    for length, speed in test:
        valid += (start, start + length - 1, speed),
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
            mx = max(mx, diff)

    print(mx)


#impl1()
