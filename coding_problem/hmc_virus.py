

import sys

K, P, N = map(int, sys.stdin.readline().split())

for _ in range(N):
    K = K*P%1000000007


print(K%1000000007)