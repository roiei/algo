



def ncr(n, r):
    if r == 0 or n == r:
        return 1
    return ncr(n-1, r-1) + ncr(n-1, r)





tc = int(input())
for t in range(tc):
    n, r = list(map(int, input().split()))
    res = ncr(n, r)
    print(res)
