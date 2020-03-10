
import time


class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stk = []
        for asteroid in asteroids:
            if not stk:
                stk += asteroid,
                continue
            
            if asteroid >= 0 and stk[-1] >= 0:
                stk += asteroid,
                continue
            
            if asteroid < 0 and stk[-1] < 0:
                stk += asteroid,
                continue
                
            stk += asteroid,
            
            while stk and stk[-1] < 0:
                val = stk.pop()
                if not stk:
                    stk += val,
                    break
                if (val >= 0 and stk[-1] >= 0) or (val < 0 and stk[-1] < 0):
                    stk += val,
                    break
                if stk[-1] == abs(val):
                    stk.pop()
                    break
                elif stk[-1] < abs(val):
                    stk[-1] = val
                else:
                    break
                    
        return stk


stime = time.time()
sol = Solution()
# print([5, 10] == sol.asteroidCollision([5, 10, -5]))
# print([] == sol.asteroidCollision([8, -8]))
# print([10] == sol.asteroidCollision([10, 2, -5]))
# print([-2, -1, 1, 2] == sol.asteroidCollision([-2, -1, 1, 2]))
print([-2, -2, -2] == sol.asteroidCollision([-2,-2,1,-2]))
# print([-2] == sol.asteroidCollision([-2,2,1,-2]))
# print([10] == sol.asteroidCollision([10,2,-5]))

print('elapse time: {} sec'.format(time.time() - stime))
