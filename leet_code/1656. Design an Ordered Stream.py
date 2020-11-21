import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
Design a stream that takes the n pairs in an arbitrary order, 
and returns the values over several calls in increasing order of their ids.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values and sets a current ptr to 1.
String[] insert(int id, String value) Stores the new (id, value) pair in the stream. 
After storing the pair:
If the stream has stored a pair with id = ptr, 
then find the longest contiguous incrementing sequence of ids starting with id = ptr and 
return a list of the values associated with those ids in order. 
Then, update ptr to the last id + 1.
Otherwise, return an empty list.

Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].

    ccccc
    3
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
    aaaaa      ccccc
    1          3
    ptr = 2

os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    aaaaa  bbbbb   ccccc
    1      2       3
    ptr = 4
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
"""

class OrderedStream:
    def __init__(self, n: int):
        self.streams = collections.defaultdict(list)
        self.ptr = 1

    def insert(self, id: int, value: str) -> [str]:
        self.streams[id] = value
        ptr = self.ptr
        res = []

        while ptr in self.streams:
            res += self.streams[ptr],
            ptr += 1

        self.ptr = ptr

        #print(res)
        return res


stime = time.time()
os = OrderedStream(5);
print([] == os.insert(3, "ccccc")); # Inserts (3, "ccccc"), returns [].
print(["aaaaa"] == os.insert(1, "aaaaa")); # Inserts (1, "aaaaa"), returns ["aaaaa"].
print(["bbbbb", "ccccc"] == os.insert(2, "bbbbb")); # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
print([] == os.insert(5, "eeeee")); # Inserts (5, "eeeee"), returns [].
print(["ddddd", "eeeee"] == os.insert(4, "ddddd")); # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].


print('elapse time: {} sec'.format(time.time() - stime))