
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


    def asteroidCollision(self, asteroids: [int]) -> [int]:
        res = []

        while asteroids:
            left = asteroids.pop()

            if not res:
                res.insert(0, left)
                continue

            res.insert(0, left)

            while res:
                left = res.pop(0)
                if not res:
                    res.insert(0, left)
                    break

                right = res.pop(0)

                if (left < 0 and right < 0) or (left >= 0 and right >= 0) \
                    or (left < 0 and right >= 0):
                    res.insert(0, right)
                    res.insert(0, left)
                    break

                # pos neg case
                if abs(left) == abs(right):
                    break
                elif abs(left) > abs(right):
                    res.insert(0, left)
                    continue
                elif abs(left) < abs(right):
                    res.insert(0, right)
                    continue

        return res


stime = time.time()
sol = Solution()
print([5, 10] == sol.asteroidCollision([5, 10, -5]))
print([] == sol.asteroidCollision([8, -8]))
print([10] == sol.asteroidCollision([10, 2, -5]))
print([-2, -1, 1, 2] == sol.asteroidCollision([-2, -1, 1, 2]))
print([-2, -2, -2] == sol.asteroidCollision([-2,-2,1,-2]))
print([-2] == sol.asteroidCollision([-2,2,1,-2]))
print([10] == sol.asteroidCollision([10,2,-5]))

print('elapse time: {} sec'.format(time.time() - stime))
