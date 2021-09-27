import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True and students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                continue
            
            students += students.pop(0),
            
            if students.count(sandwiches[0]) == 0:
                break
        
        return len(students) if students else 0


stime = time.time()
print(0 == Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print('elapse time: {} sec'.format(time.time() - stime))