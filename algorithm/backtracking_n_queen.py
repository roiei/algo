

def n_queen(q, n, row):
    # pruning by back tracking
    if row >= 1:
        for i in range(row):
            if (row-i == abs(q[row]-q[i]) or q[row] == q[i]):
                return False

    if row == n-1:
        print(q)
        return

    for i in range(n):
        q[row+1] = i
        n_queen(q, n, row+1)

n = 4
q = [-1 for i in range(n)]

for i in range(n):
    q[0] = i
    n_queen(q, n, 0)
