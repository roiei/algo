


#n = 6
#events = [(3, 5), (5, 5), (2, 3)]
#events = [[3, 5], [5, 5], [2, 3]]


n = int(input())
num_event = int(input())
events = []
for i in range(num_event):
    events.append(list(map(int, input().split())))

car1 = (1, 1)
car2 = (n, n)

cache_cost = {}
cache_path = {}

def func(n, car1, car2, which_car, events):
    global cache_cost
    global cache_path
    idx = str(which_car)
    for evt in events:
        idx += str(evt)
    if idx in cache_cost:
        #print('cache_cost...', cache_cost[idx])
        return cache_path[idx], cache_cost[idx]
    if not events:
        return [], 0
    path = []
    cur_event = events.pop(0)
    path1, res1 = func(n, car1, car2, 1, events[:])
    path2, res2 = func(n, car1, car2, 2, events[:])
    path = []
    if res1 < res2:
        min_cost = res1
        path.extend(path1)
    else:
        min_cost = res2
        path.extend(path2)

    evt_x, evt_y = cur_event
    c_x, c_y = (0, 0)
    if 1 == which_car:
        c_x, c_y = car1
    else:
        c_x, c_y = car2
    dist = abs(evt_x - c_x) + abs(evt_y - c_y)
    path.append(which_car)
    cache_cost[idx] = min_cost + dist
    cache_path[idx] = path
    return path, cache_cost[idx]


path1, res1 = func(n, car1, car2, 1, events[:])
path2, res2 = func(n, car1, car2, 2, events[:])
path = []
if res1 < res2:
    min_cost = res1
    path.extend(path1)
else:
    min_cost = res2
    path.extend(path2)
print(min_cost)
path.reverse()
for i in path:
    print(i)

