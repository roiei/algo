import sys


N = 3
schedules = [
    [1, 3],
    [2, 4],
    [3, 5],
]

# N = int(sys.stdin.readline())
# schedules = []
# for _ in range(N):
#     schedules += list(map(int, sys.stdin.readline().split())),

schedules.sort(key=lambda p: p[1])

start, end = schedules.pop(0)
cnt = 1

while schedules:
    while schedules and end > schedules[0][0]:
        schedules.pop(0)

    if schedules:
        start, end = schedules.pop(0)
        cnt += 1

print(cnt)


