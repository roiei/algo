import time

class Solution:
    def calPoints(self, ops: 'List[str]') -> int:
        ptrs = []
        for op in ops:
            if 'C' == op:
                ptrs.pop()
                pass
            elif 'D' == op:
                ptrs.append(ptrs[-1]*2)
                pass
            elif '+' == op:
                ptrs.append(ptrs[-1]+ptrs[-2])
                pass
            else:
                ptrs.append(int(op))
        return sum(ptrs)

stime = time.time()
sol = Solution()
print(30 == sol.calPoints(["5","2","C","D","+"])) # 30
print(27 == sol.calPoints(["5","-2","4","C","D","9","+","+"])) # 27
print('elapse time: {} sec'.format(time.time() - stime))