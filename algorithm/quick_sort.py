

import random


def partition(a, n, base):
    v = a[base + n - 1]    # v is pivot value; value at the last 
    i = 0           # from left
    j = n - 2       # from right

    while True:
        while a[base + i] < v:
            i+= 1
        while a[base + j] > v:
            j-= 1
        if i < j:
            a[base + i], a[base + j] = a[base + j], a[base + i]
        else:
            break

    a[base + n-1], a[base + i] = a[base + i], a[base + n-1]
    return i

def quick_sort(a, n, base):
    if n <= 1:
        return
    
    #pivot = random.randint(0, n-1)
    #a[pivot], a[n-1] = a[n-1], a[pivot]

    i = partition(a, n, base)
    quick_sort(a, i, base)
    quick_sort(a, n - i - 1, i + 1)

def partition_nr(a, first, last):
    v = a[last]
    i = first
    j = last - 1
    while True:
        while a[i] < v:
            i+= 1
        while a[j] > v:
            j-= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[last], a[i] = a[i], a[last]
    return i

def quick_sort_nr(a, n, base):
    stack = []
    stack.append(n - 1)             # last index
    stack.append(0)                 # first index
    while stack:
        first = stack.pop()         # first
        last  = stack.pop()         # last
        if last - first + 1 > 1:
            i = partition_nr(a, first, last)
            stack.append(last)      # right last
            stack.append(i + 1)     # right first
            stack.append(i - 1)     # left last
            stack.append(first)     # left first

def quick_sort_nr_r(a, n, base):
    stack = []
    stack.append(n - 1)             # last index
    stack.append(0)                 # first index
    while stack:
        first = stack.pop()         # first
        last  = stack.pop()         # last
        if last - first + 1 > 1:
            pivot = random.randint(first, last-1)
            a[pivot], a[last] = a[last], a[pivot]

            i = partition_nr(a, first, last)
            stack.append(last)      # right last
            stack.append(i + 1)     # right first
            stack.append(i - 1)     # left last
            stack.append(first)     # left first

def quick_sort_nr_mot(a, n, base):
    stack = []
    stack.append(n - 1)             # last index
    stack.append(0)                 # first index
    while stack:
        first = stack.pop()         # first
        last  = stack.pop()         # last
        if last - first + 1 > 1:
            tmp = sorted([a[first], a[last//2], a[last]])
            a[last], a[last//2] = tmp[1], tmp[2]
            i = partition_nr(a, first, last)
            stack.append(last)      # right last
            stack.append(i + 1)     # right first
            stack.append(i - 1)     # left last
            stack.append(first)     # left first

def quick_sort_nr_insert(a, n, base):
    stack = []
    stack.append(n - 1)             # last index
    stack.append(0)                 # first index
    while stack:
        first = stack.pop()         # first
        last  = stack.pop()         # last
        if last - first + 1 > 1:
            if last - first > 200:
                i = partition_nr(a, first, last)
                stack.append(last)      # right last
                stack.append(i + 1)     # right first
                stack.append(i - 1)     # left last
                stack.append(first)     # left first
            else:
                sort_insert(a, last - first)

a = []
for ch in 'ALGORITHM':
    a.append(ch)

#a = [7, 11, 5, 1, 9, 3]
quick_sort(a, len(a), 0)
print(a)
a = []
for ch in 'ALGORITHM':
    a.append(ch)
#a = [7, 11, 5, 1, 9, 3]
quick_sort_nr_r(a, len(a), 0)
print(a)

a = []
for ch in 'ALGORITHM':
    a.append(ch)
quick_sort_nr_mot(a, len(a), 0)
print(a)
