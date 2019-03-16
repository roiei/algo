

def get_moving_avg(a, m):
    if len(a) < m:
        return None
    avgs = []
    for i in range(0, len(a) - m):
        avgs.append(sum(a[i:i+m]) / m)
    return avgs

a = [2, 4, 2, 3, 1, 5, 7, 8, 9]
m = 4
print(get_moving_avg(a, m))



def select_sort(a, n):
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if a[minidx] < a[j]:
                minidx = j
        a[minidx], a[i] = a[i], a[minidx]

