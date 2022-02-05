
#N, M, K = 5, 20, 4
#lines = [5, 8, 10, 19, 7]

N, M, K = 9, 25, 50
lines = [1, 21, 2, 22, 3, 23, 4, 24, 10]


N, M, K = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))


def get_sum(lines, K):
    cur = 0
    idx = 0
    tot = 0

    while K:
        inc = 0
        while cur + lines[idx] <= M:
            cur += lines[idx]
            inc += lines[idx]
            idx = (idx + 1)%len(lines)

        tot += inc
        cur = 0
        K -= 1

    return tot


seqs = []

def dfs(seq, sel, seqs):
    if len(sel) == N:
        seqs += seq,
        return

    for i in range(N):
        if i in sel:
            continue

        dfs(seq + [lines[i]], sel + [i], seqs)

dfs([], [], seqs)

mn = float('inf')
for seq in seqs:
    mn = min(mn, get_sum(seq, K))

print(mn)