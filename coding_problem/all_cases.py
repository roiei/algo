

n = 7
cnt = 0
for i in range(n):
    print(i)
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                print('{:-2}:{:-2}:{:-2}:{:-2}'.format(i, j, k, l))
                cnt += 1
print(cnt)


def print_picked(picked):
    for i in range(0, len(picked), 4):
        print('{:-2}:{:-2}:{:-2}:{:-2}'.format(picked[i], picked[i+1], picked[i+2], picked[i+3]))

def pick(n, picked, to_pick):
    if to_pick == 0:
        print_picked(picked)
        return
    smallest = 0 if len(picked) == 0 else picked[len(picked)-1] + 1
    for next in range(smallest, n):
        picked.append(next)             # 0, 1, 2, 3
        pick(n, picked, to_pick - 1)    # 0, 1, 2, 3  <- print
        picked.pop(len(picked)-1)       # 0, 1, 2 

picked = []
pick(n, picked, 4)