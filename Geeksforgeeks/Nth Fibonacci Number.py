import time
import ast


def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

mem = {}
def fib_mem(n):
    if n in mem:
        return mem[n]
    if n < 3:
        return 1
    mem[n] = fib_mem(n-1) + fib_mem(n-2)
    return mem[n]

def fib_tab(n):
    if n < 3:
        return 1
    dp = [1]*(n)
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


tc = int(input())
for i in range(tc):
    n = int(input())
    ret = fib_mem(n)%1000000007
    print(ret)


n = 40

print(fib(n))
print(fib_mem(n))
print(fib_tab(n))
