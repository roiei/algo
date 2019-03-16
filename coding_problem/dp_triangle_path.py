

tri_in = [
[6],
[1,2],
[3,7,4],
[9,4,1,7],
[2,7,5,9,4]
]

tri_in = [
[1],
[2, 4],
[8, 16, 8],
[32, 64, 32, 64],
[128, 256, 128, 256, 128]
]

class Res:
    def __init__(self):
        self.acc = 0

def get_max_sum(triangle, depth, l, x, sum):
    global g_call_cnt
    g_call_cnt += 1

    if depth == l+1:
        return sum + triangle[l][x] # leaf, return current value
    sum += triangle[l][x]
    return max(get_max_sum(triangle, depth, l+1, x, sum), \
        get_max_sum(triangle, depth, l+1, x+1, sum))


tri_cache = [[-1 for j in range(len(tri_in[len(tri_in)-1]))] for i in range(len(tri_in))]

def get_max_sum_dp(triangle, depth, l, x):
    global g_call_cnt
    g_call_cnt += 1

    if depth == l+1:
        return triangle[l][x] # leaf, return current value
    if -1 != tri_cache[l][x]:
        return tri_cache[l][x]
    tri_cache[l][x] = max(get_max_sum_dp(triangle, depth, l+1, x), \
        get_max_sum_dp(triangle, depth, l+1, x+1)) + triangle[l][x]
    return tri_cache[l][x]

g_call_cnt = 0
print(get_max_sum(tri_in, len(tri_in), 0, 0, 0))
print(g_call_cnt)

g_call_cnt = 0
print(get_max_sum_dp(tri_in, len(tri_in), 0, 0))
print(g_call_cnt)
