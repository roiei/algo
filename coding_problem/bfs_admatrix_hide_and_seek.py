max_num = 100000
locations = [0 for i in range(max_num+1)]

def func(n, k, locations):
    global max_num
    q = []
    locations[n] = 0
    q.append(n)
    cnt = 0
    while q:
        cn = q.pop(0)
        if cn == k:
            break
        if cn > 0 and locations[cn-1] == 0:
            locations[cn-1] = locations[cn]+1
            q.append(cn-1)
        if cn < max_num and locations[cn+1] == 0:
            locations[cn+1] = locations[cn]+1
            q.append(cn+1)
        if 2*cn <= max_num and locations[2*cn] == 0:
            locations[2*cn] = locations[cn]+1
            q.append(2*cn)
        cnt += 1
    print(locations[k])

import sys
n, k = map(int, sys.stdin.readline().split())
func(n, k, locations)