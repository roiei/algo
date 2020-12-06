from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        left = n
        n = len(flowerbed)

        for i in range(n):
            if not left:
                break
            if i == 0:
                if flowerbed[i] == 0 and ((i + 1 < n and flowerbed[i+1] == 0) or \
                        i + 1 == n):
                    flowerbed[i] = 1
                    left -= 1
            elif i == n - 1:
                if flowerbed[i] == 0 and (i - 1 >= 0 and flowerbed[i-1] == 0):
                    flowerbed[i] = 1
                    left -= 1
            else:
                if flowerbed[i] == 0 and (flowerbed[i-1] == 0 and \
                        flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    left -= 1

        return True if left == 0 else False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        
        i = 1
        while i < len(flowerbed) - 1 and n:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1
        
        return n == 0



flowerbed = [1,0,0,0,1]
n = 1

# flowerbed = [1,0,0,0,1]
# n = 2


# flowerbed = [1,0,1,0,1,0,1]
# n = 1

flowerbed = [0,0,0,0,0,1,0,0]
n = 0

sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))

