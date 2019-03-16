

def bino(n, r):
    if r == 0 or n == r:
        return 1
    return bino(n-1, r-1) + bino(n-1, r)


n = 4
r = 2

n = 100
r = 20


bino_cache = [[-1 for i in range(r)] for j in range(n)]

def bino_dp(n, r):
    if r == 0 or n == r:
        return 1
    if -1 != bino_cache[n-1][r-1]:
        return bino_cache[n-1][r-1]
    bino_cache[n-1][r-1] = bino_dp(n-1, r-1) + bino_dp(n-1, r)
    return bino_cache[n-1][r-1]



#print(bino(n, r))
print(bino_dp(n, r))


n = 2500
cache = [[-1 for i in range(n)] for j in range(n)]


# def some_obsecure_func(a, b):
#      if ...:
#         return ...

#     if -1 != cache[a][b]:
#         return cache[a][b]

#     cache[a][b] = some_obsecure_func(a..., b...)
#     return cache[a][b]