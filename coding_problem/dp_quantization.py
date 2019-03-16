

import math


vals = [3, 3, 3, 1, 2, 3, 2, 2, 2, 1]
vals = [1, 744, 755, 4, 897, 702, 890, 6, 777]
s = 3

max_val = max(vals)
min_val = min(vals)

unit = max_val // s
print('unit = ', unit)

outvals = []
for val in vals:
    min_diff = max_val+1
    qval = -1
    for si in range(1, s+1):
        diff = math.sqrt((val - unit*si)*(val - unit*si))
        if min_diff > diff:
            min_diff = diff
            qval = si
    if -1 != qval:
        outvals.append(qval)

print(outvals)

mse = 0
for i in range(len(vals)):
    mse += math.sqrt((vals[i] - outvals[i])*(vals[i] - outvals[i]))
print('mse = ', mse)

print(list(zip(vals, outvals)))
#print(diff.pop(1))
