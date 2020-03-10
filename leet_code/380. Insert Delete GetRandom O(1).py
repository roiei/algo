import time
import random


class RandomizedSet:
    def __init__(self):
        self.data = {}
        self.linear_data = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = val
        self.linear_data.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        del self.data[val]
        del self.linear_data[self.linear_data.index(val)]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        return self.linear_data[random.randint(0, self.n-1)]

obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())


stime = time.time()
#print(Solution().countRangeSum([-2,5,-1], -2, 2))
#print(Solution().countRangeSum([2147483647,-2147483648,-1,0], -1, 0)) # 4
print('elapse time: {} sec'.format(time.time() - stime))

