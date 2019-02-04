




def select_min_linear(a, n, k):
    '''
    This is not sort function
    it is used to find the min value
    '''
    for i in range(n-1):
        minidx = i
        minval = a[i]
        for j in range(i+1, n):
            if minval > a[j]:
                minval = a[j]
                minidx = j
        a[minidx] = a[i]
        a[i] = minval
        if i == k:
            return minval

def partition(a, l, r, base):
    pv = a[base + r - 1]
    i = l
    j = r - 1
    while True:
        while a[base + i] < pv: i+= 1
        while a[base + j] > pv: j-= 1
        if i >= j:
            break
        a[base + i], a[base + j] = a[base + j], a[base + i]
    a[base + r - 1], a[base + i] = a[base + i], a[base + r - 1]
    return i

def selection_partition(a, n, k):
    '''
    k : kth elem to find
    '''
    l = 1
    r = n - 1
    while r > l:
        v = a[r]
        i = l
        j = r - 1
        while True:
            while a[i] < v: i += 1
            while a[j] > v: j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        if i >= k: r = i - 1
        if i <= k: l = i + 1
    return a[i]

def sort_select(a, n):
    for i in range(n-1):
        minval = a[i]
        minidx = i
        for j in range(i+1, n):
            if minval > a[j]:
                minval = a[j]
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]

def sort_insert(a, n):
    for i in range(1, n):
        t = a[i]
        j = i
        while a[j-1] > t and j > 0:
            a[j] = a[j-1]
            j -= 1
        a[j] = t

def sort_boubble(a, n):
    for i in range(n - 1):
        for j in range(1, n - i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]

a = [] 
for ch in 'ALGORITHM':
    a.append(ch)
a = [7, 11, 5, 1, 9, 3]
print(sort_select(a, len(a)))
print(a)

a = [7, 11, 5, 1, 9, 3]
print(sort_insert(a, len(a)))
print(a)

a = [7, 11, 5, 1, 9, 3]
print(sort_boubble(a, len(a)))
print(a)


# print(selection_partition(a, len(a), 0, 0))

# a = [7, 11, 5, 1, 9, 3]
# print(selection_partition(a, len(a), 1, 0))

# a = [7, 11, 5, 1, 9, 3]
# print(selection_partition(a, len(a), 2, 0))

# a = [7, 11, 5, 1, 9, 3]
# print(selection_partition(a, len(a), 3, 0))

# a = [7, 11, 5, 1, 9, 3]
# print(selection_partition(a, len(a), 4, 0))
#print(a)