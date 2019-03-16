

import math


vals = [3, 3, 3, 1, 2, 3, 2, 2, 2, 1]
s = 3

max_val = max(vals)
min_val = min(vals)

unit = max_val // s

for val in vals:
diff = {}
    min_diff = s*s+1
    idx = -1
    for si in range(1, s+1):
        diff = math.sqrt((3 - unit*si)*(3 - unit*si))
        if min_diff > diff:
            min_diff = diff
            idx = si-1
    if -1 != idx:
        print('min_diff = ', idx)
#print(diff.pop(1))
