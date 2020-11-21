
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



#code

mem = {}
def knapsack(items, pos, n, cap, value):
    if pos == n:
        return value
    if (pos, cap) in mem:
        return mem[(pos, cap)]

    val1 = knapsack(items, pos+1, n, cap, value)
    val2 = -1
    if cap - items[pos][1] >= 0:
        val2 = knapsack(items, pos+1, n, cap - items[pos][1], value + items[pos][0])
    mem[(pos, cap)] = max(val1, val2)
    return mem[(pos, cap)]

def kanpsack_ref(items, pos, n, cap):
    if pos == n:
        return 0
    if (pos, cap) in mem:
        return mem[(pos, cap)]
    ret = 0
    if items[pos][1] <= cap:
        ret = kanpsack_ref(items, pos+1, n, cap - items[pos][1]) + items[pos][0]
    mem[(pos, cap)] = max(ret, kanpsack_ref(items, pos+1, n, cap))
    return mem[(pos, cap)]


def knapsack_dp(w, p, n, m):
    """
    w : weight of items
    p : profit of itmes
    n : number of items
    m : bag's size
    """
    cost = [0]*(m+1)      # cost by step

    for j in range(n):                  # number of items to try
        for y in range(1, m+1, 1):      # increase the size of bag
            if y >= w[j]:               # if possible to put item j in the bag with size y 
                if cost[y] < cost[y - w[j]] + p[j]:
                    cost[y] = cost[y - w[j]] + p[j]

    return cost[m] 

def knapsack_mine_duplicate(n, weights, values, capacity):
    dp = [0]*(capacity+1)
    for i in range(n):
        for j in range(weights[i], capacity+1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

def knapsack(n, weights, values, capacity):
    dp = [[0]*(capacity+1) for i in range(n+1)]
    for i in range(capacity+1):
        dp[0][i] = 0

    weights = [0] + weights
    values = [0] + values

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if w == 0:
                dp[i][w] = 0
            if w < weights[i]:
                dp[i][w] = dp[i-1][w]
            if w >= weights[i]:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i]] + values[i])

    return dp[n][capacity]


num_t = 1#int(input())
for cnt_t in range(num_t):
    n = 58#int(input())
    capacity = 41#int(input())
    
    values = [57,95,13,29,1,99,34,77,61,23,24,70,73,88,33,61,43,5,41,63,8,67,20,72,98,59,46,58,64,94,97,70,46,81,42,7,1,52,20,54,81,3,73,78,81,11,41,45,18,94,24,82,9,19,59,48,2,72]#list(map(int, input().split()))
    weights = [83,84,85,76,13,87,2,23,33,82,79,100,88,85,91,78,83,44,4,50,11,68,90,88,73,83,46,16,7,35,76,31,40,49,65,2,18,47,55,38,75,58,86,77,96,94,82,92,10,86,54,49,65,44,77,22,81,52]#list(map(int, input().split()))
    
    #print(items)
    #print(knapsack(items, 0, len(items), capacity, 0))


    # n = 3
    # capacity = 4
    # weights = [1, 2, 3]
    # values = [4, 5, 1]

    items = []
    for i in range(n):
        items += [values[i], weights[i]],


    mem = {}
    print(kanpsack_ref(items, 0, len(items), capacity))
    #print(knapsack_dp(weights, values, n, capacity))
    print(knapsack(n, weights, values, capacity))
    
    

