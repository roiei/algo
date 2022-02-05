

K, P, N = 2, 3, 2
K, P, N = 1, 2, 1


def dfs(exp):
    if exp in mem:
        return mem[exp]

    if exp == 1:
        return P%1000000007

    part = exp//2

    mem[exp] = (dfs(part)*dfs(part + exp%2))%1000000007
    return mem[exp]

mem = {}
res = (K*dfs(N*10))%1000000007
print(res)
