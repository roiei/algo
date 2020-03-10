class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.n = 0
        self.data = {}
        self.lru = []

    def get(self, key):
        if key not in self.data:
            return -1
        retval = self.data[key]
        self.lru.remove(key)
        self.lru[0:0] = [key]
        return retval
        
    def put(self, key, value):
        if key not in self.data and self.n == self.capacity:
            self.data.pop(self.lru[-1])
            self.lru.pop()
            self.n -= 1

        if key in self.data:
            self.lru.pop(self.lru.index(key))
            self.n -= 1

        self.data[key] = value
        self.lru[0:0] = [key]
        self.n+= 1


cache = LRUCache(2)

cache.put(2, 1);
cache.put(1, 1);
cache.put(2, 3);
cache.put(4, 1);
print(cache.get(1));
print(cache.get(2));