
class Item:
    def __init__(self, name, w, p):
        self.name = name
        self.w = w
        self.p = p


def knapsack(items, m):
    if len(items) == 0:
        return 0

    # for item in items:


    # knapsack(items.pop(), m)


def knapsack_dp(name, w, p, n, m):
    """
    name : name of items
    w : weight of items
    p : profit of itmes
    n : number of items
    m : bag's size
    """
    cost = [0 for i in range(m+1)]      # cost by step
    best = [-1 for i in range(m+1)]

    for j in range(n):                  # number of items to try
        for y in range(1, m+1, 1):      # increase the size of bag
            if y >= w[j]:               # if possible to put item j in the bag with size y 
                if cost[y] < cost[y - w[j]] + p[j]:
                    cost[y] = cost[y - w[j]] + p[j]
                    best[y] = j

    # when item 1 case
    # bag size 1
    # cost[1] = cost[0] + p[1]
    # bag size 2
    # cost[2] = cost[1] + p[1]
    # ...
    # when item 2 case
    # bag size 1
    #   cost[2] == 2
    # if 2 >= w[j] <-- 2
    #     if cost[2] = cost[2 - 2] + p[j] <- 3
    #


    y = m
    print(name[best[y]])
    y -= w[best[y]]
    
    while y > 0 and best[y] >= 0:
        print(name[best[y]])
        y -= w[best[y]]

    return cost[m]



