

def search_binary(a, left, right, key):
    while right >= left:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        if key > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find(a, n, key):
    left = 0
    right = n - 1
    return search_binary(a, left, right, key)

def find_first(a, n, key):
    idx = find(a, n, key)
    if idx == -1:
        return False
    for i in range(idx, 0, -1):
        if key != a[i]:
            if idx != i:
                idx = i + 1
            break
    return idx

def insert(a, n, value):
    for i in range(n-1, 1, -1):
        if a[i-1] <= value:
            a[i] = value
            break
        a[i] = a[i-1]
    return True

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(a)
print('find 4 = ', find(a, len(a), 4))
print('find 9 = ', find(a, len(a), 9))
print('insert 4')
insert(a, len(a), 4)
print(a)
print('find 4 = ', find(a, len(a), 4))
print('find 9 = ', find(a, len(a), 9))
print('insert 4')
insert(a, len(a), 4)
print(a)
print('find_first 4 = ', find_first(a, len(a), 4))
print('find 4 = ', find(a, len(a), 4))

print('insert 4')
insert(a, len(a), 4)
print(a)
print('find_first 4 = ', find_first(a, len(a), 4))
print('find 4 = ', find(a, len(a), 4))