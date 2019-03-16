
#from ..data_structure.prio_queue import *

import math

# weights = [
# 100,
# 90,
# 200
# ]

# weights = [
# 45,
# 55,
# 70,
# 60,
# 50,
# 75
# ]

# weights = [
# 92,
# 56,
# 47,
# 82
# ]

# weights = [
# 2,
# 3,
# 4,
# 7,
# 8
# ]

weights = [
50,
50,
100,
200
]


# 1. get total's avg
# 2. find among p1, p2, which one's accumulation is close to the avg
# 3. get the biggest one and add it to the less one
# 4. 


weights.sort(reverse=True)
print(weights)

avg = sum(weights)//2

part1 = 0
part2 = 0

# if 0 != len(weights) % 2:
#     weights.append(0)

while weights:
    print('avg {}, part1 {}, part2 {}'.format(avg, part1, part2))
    if avg - part1 < avg - part2:
        part2 += weights.pop(0)
    else:
        part1 += weights.pop(0)

print(part1, part2)




