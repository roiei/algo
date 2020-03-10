

class Solution:
    def isHappy(self, n: int) -> bool:
        repeat = []
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in repeat:
                return False
            repeat += n,
        return True

