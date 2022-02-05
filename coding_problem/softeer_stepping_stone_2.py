from typing import List
import bisect


N = 5
stones = [3, 2, 4, 5, 1]

i = 0
mx = 0

peak = max(stones)


def find_list(stones):
    values = []
    forward = [0]*N

    for i, stone in enumerate(stones):
        if not values:
            values += stone,
            forward[i] = len(values)
            continue

        if values[-1] < stone:
            values += stone,
            forward[i] = len(values)
            continue

        idx = bisect.bisect_left(values, stone)
        values[idx] = stone
        forward[i] = idx + 1

    return forward


forward = find_list(stones)
backward = find_list(stones[::-1])
mx = 0

for i in range(N):
    felem = forward[i]
    belem = backward[N - 1 - i]

    if not felem or not belem:
        continue

    mx = max(mx, felem + belem - 1)

print(mx)



