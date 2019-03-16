class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 10000
        self.hash_tbl = [[] for i in range(self.n)]
        
    def add(self, key: 'int') -> 'None':
        if True == self.contains(key):
            return False
        index = key % self.n
        self.hash_tbl[index].insert(0, key)
        return True

    def remove(self, key: 'int') -> 'None':
        index = key % self.n
        found_idx = -1
        for i in range(len(self.hash_tbl[index])):
            if key == self.hash_tbl[index][i]:
                found_idx = i
                break
        if -1 != found_idx:
            del self.hash_tbl[index][found_idx]
            #self.hash_tbl[index].pop(found_idx)
            return True
        return False
        

    def contains(self, key: 'int') -> 'bool':
        """
        Returns true if this set contains the specified element
        """
        found = False
        index = key % self.n
        for i in range(len(self.hash_tbl[index])):
            if key == self.hash_tbl[index][i]:
                found = True
                break
        return found


# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet();
hashSet.add(1);         
hashSet.add(2);

print('contain 1 = ', hashSet.contains(1));    # returns true
print('contain 3 = ', hashSet.contains(3));    # returns false (not found)
hashSet.add(2);         #
print('contain 2 = ', hashSet.contains(2));    # returns true
print('remove  2 = ', hashSet.remove(2));      #  
print('contain 2 = ', hashSet.contains(2));    # returns false (already removed)