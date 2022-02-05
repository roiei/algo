import sys


gears = list(map(int, sys.stdin.readline().split()))

pre = gears[0]
order = 'mixed'

for i in range(1, len(gears)):
    if pre >= gears[i]:
        break

    pre = gears[i]
else:
    order = 'ascending'


for i in range(1, len(gears)):
    if pre <= gears[i]:
        break

    pre = gears[i]
else:
    order = 'descending'

print(order)