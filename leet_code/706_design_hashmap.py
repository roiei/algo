
# class Solution:
#     def reverse(x: 'int') -> 'int':

# sol = Solution()
# print(sol.reverse(x))

# class MyHashMap:
#     class Item:
#         def __init__(self, key, value):
#             self.state = 'EMPTY'
#             self.key = key
#             self.value = value

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.n = 1000000
#         self.tbl = [self.Item('EMPTY', 0) for i in range(self.n)]
#         self.hash_func = lambda val: val

#     def put(self, key: 'int', value: 'int') -> 'None':
#         """
#         value will always be non-negative.
#         """
#         idx = self.find(key)
#         if -1 != idx:
#             self.tbl[idx].key = key
#             self.tbl[idx].value = value
#             return
#         no_empty = False
#         start = index = self.hash_func(key) % self.n
#         while self.tbl[index].state != 'EMPTY':
#             index = self.hash_func(index + 1) % self.n
#             if index == start:
#                 no_empty = True
#                 break
#         if True == no_empty:
#             return
#         self.tbl[index].key = key
#         self.tbl[index].value = value
#         self.tbl[index].state = 'FILLED'
#         #print('put: tbl[{}] = ({}, {}, {})'.format(index, key, value, 'FILLED'))

#     def find(self, key) -> 'index:int':
#         start = index = self.hash_func(key) % self.n
#         not_found = False
#         while True:
#             if self.tbl[index].state == 'FILLED' and self.tbl[index].key == key:
#                 break
#             index = self.hash_func(key) % self.n
#             if start == index:
#                 not_found = True
#                 break
#         if True == not_found:
#             return -1
#         return index

#     def get(self, key: 'int') -> 'int':
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         idx = self.find(key)
#         #print('get: find: {}'.format(idx))
#         if -1 == idx:
#             return -1
#         return self.tbl[idx].value

#     def remove(self, key: 'int') -> 'None':
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         idx = self.find(key)
#         if -1 == idx:
#             return
#         self.tbl[idx].state = 'EMPTY'


class MyHashMap:
    def __init__(self):
        self.n = 100
        self.data = [[] for _ in range(self.n)]
        self.hash_func = lambda p: p
    
    def search(self, key):
        idx = self.hash_func(key)%self.n
        for i, item in enumerate(self.data[idx]):
            k, v = item
            if k == key:
                return i
        return -1
        
    def put(self, key: int, value: int) -> None:
        idx = self.hash_func(key)%self.n
        lidx = self.search(key)
        if -1 == lidx:
            self.data[idx] += (key, value),
            return
        
        self.data[idx][lidx] = (key, value)

    def get(self, key: int) -> int:
        idx = self.hash_func(key)%self.n
        lidx = self.search(key)
        if -1 == lidx:
            return -1
        
        return self.data[idx][lidx][1]

    def remove(self, key: int) -> None:
        idx = self.hash_func(key)%self.n
        lidx = self.search(key)
        if -1 == lidx:
            return

        self.data[idx].pop(lidx)


hashMap = MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
print(hashMap.get(1));            # returns 1
print(hashMap.get(3));            # returns -1 (not found)
hashMap.put(2, 1);                # update the existing value
print(hashMap.get(2));            # returns 1 
hashMap.remove(2);                # remove the mapping for 2
print(hashMap.get(2));            # returns -1