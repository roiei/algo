


# N killo gram
# 3K-bag, 5K-bag

# least number of bags

# ex. 18 K -> 



g_depths = []
def calc(n, depth):
    #print('n = ', n, ' depth = ', depth)
    if n < 3:
        if n == 0:
            g_depths.append(depth)
        return n

    res_5 = n-3
    if n >= 5:
        res_5 = calc(n-5, depth+1)
    res_3 = calc(n-3, depth+1)
    #print('n = ', n, ' -> ', res_3, res_5)
    minval = min(res_3, res_5)
    return minval


g_depths = []
g_sugar_cache = []
def get_optimal_num_bags(n, depth):
    #print('n = ', n, ' depth = ', depth)
    if -1 != g_sugar_cache[n]:
        return g_sugar_cache[n]
    if n < 3:
        if n == 0:
            g_depths.append(depth)
        return n
    res_5 = n-3
    if n >= 5:
        res_5 = get_optimal_num_bags(n-5, depth+1)
    res_3 = get_optimal_num_bags(n-3, depth+1)
    #print('n = ', n, ' -> ', res_3, res_5)
    minval = min(res_3, res_5)
    g_sugar_cache[n] = minval
    return minval

n = int(input())
g_sugar_cache = [-1 for i in range(n + 1)]
res = get_optimal_num_bags(n, 0)
if res != 0:
    print(-1)
else:
    print(min(g_depths))


# class InSet:
#     def __init__(self, inval, out):
#         self.inval = inval
#         self.out = out

# in_set = {InSet(18,4), InSet(4,-1), InSet(6,2), InSet(9,3), InSet(11,3)}
# for in_item in in_set:
#     g_sugar_cache = [-1 for i in range(in_item.inval + 1)]
#     g_depths = []
#     print('in_item.inval = {}, in_item.out = {}'.format(in_item.inval, in_item.out))
#     res = get_optimal_num_bags(in_item.inval, 0)
#     if res != 0:
#         if in_item.out != -1:
#             print('WRONG')
#     else:
#         if in_item.out != min(g_depths):
#             print('WRONG')


