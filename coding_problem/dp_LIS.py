
import time


# Longest Increasing Subsequence

g_lis_cnt = 0


#seq = [1, 3, 4, 2, 4]
seq = [1, 12, 9, 4, 2, 5, 3, 7, 9, 11]
#seq = [9, 1, 2, 3, 4, 5, 6, 21, 28, 19]

#seq = [9, 1, 3, 4, 2, 4, 5, 0, 7]


def lis(a):
    if not a:
        return 0
    ret = 0
    for i in range(len(a)):
        b = []
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                b.append(a[j])
        ret = max(ret, 1 + lis(b))
    return ret

def lis_3(a, prev):
    if not a:
        return 0
    if a[0] <= prev:
        return 0
    cur_max = 1
    for i in range(len(a)):
        b = []
        for j in range(i+1, len(a)):
            if a[i] < a[j]:        # this line garantee the increasing part!
                b.append(a[j])
        cur_max = max(cur_max, lis_3(b, a[i]) + 1)
    return cur_max

    def jlis(idx_a, idx_b):
        if -1 != cache[idx_a+1][idx_b+1]:
            return cache[idx_a+1][idx_b+1]
        ret = 2
        a_val = NEGINF if idx_a == -1 else a[idx_a]
        b_val = NEGINF if idx_b == -1 else b[idx_b]
        max_elem = max(a_val, b_val)

        for next_a in range(idx_a+1, n):
            if max_elem < a[next_a]:
                ret = max(ret, jlis(next_a, idx_b) + 1)
        for next_b in range(idx_b+1, m):
            if max_elem < a[next_b]:
                ret = max(ret, jlis(idx_a, next_b) + 1)
        return ret


# g_lis_cnt = 0
# lis_cache = [-1 for i in range(len(seq))]
# print(find_lis_dp(seq, len(seq), 0, 0))
# print('cnt = ', g_lis_cnt)
stime = time.time()
print(seq)
print(lis(seq))
#print(lis_3(seq, 0))
print('elapse time: {} sec'.format(time.time() - stime))
