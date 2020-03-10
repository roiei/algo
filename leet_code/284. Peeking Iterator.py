# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.data = []
        self.n = 0
        self.cur = 0
        while True == iterator.hasNext():
            self.data += iterator.next(),
            self.n += 1
        
    def peek(self):
        if self.cur < self.n:
            return self.data[self.cur]
        return -1
        
    def next(self):
        ret = -1
        if self.cur < self.n:
            ret = self.data[self.cur]
            self.cur += 1
        return ret
            
    def hasNext(self):
        return True if self.cur < self.n else False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].