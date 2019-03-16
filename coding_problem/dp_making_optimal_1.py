import sys

n = int(input())

if n < 1 or n > 1000000:
    print(1)
    sys.exit()

g_cache = []
count = 1
stack = []
stack.append(n)
next_stack = []
g_cache = [-1 for i in range(n+1)]

while True:
    while stack:
        i = stack.pop()
        if -1 != g_cache[i]:
            continue
        g_cache[i] = 1
        if i < 1:
            continue
        if i%3 == 0 and i != 0:
            next_stack.append(i//3)
        if i%2 == 0 and i != 0:
            next_stack.append(i//2)
        next_stack.append(i-1)
    
    if min(next_stack) == 1:    # the first 1 denotes the optimal path
        break
    stack = next_stack[:]
    next_stack.clear()
    count += 1

print(count)