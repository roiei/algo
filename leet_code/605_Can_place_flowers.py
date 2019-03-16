
class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        flowerbed
        left = n
        for i in range(len(flowerbed)):
            if i > 0 and i < len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and (i+1 < len(flowerbed)-1 and 0 == flowerbed[i+1]):
                    flowerbed[i] = 1
                    left -= 1
                    print('set: i = {}'.format(i))
            elif i == 0:
                if 0 == flowerbed[i] and ((i+1 < len(flowerbed)-1 and 0 == flowerbed[i+1]) or i+1 == len(flowerbed)):
                    flowerbed[i] = 1
                    left -= 1
                    print('set: i = {}'.format(i))
            elif i == len(flowerbed)-1:
                if 0 == flowerbed[i] and ((i-1 >= 0) and 0 == flowerbed[i-1]):
                    flowerbed[i] = 1
                    left -= 1
                    print('set: i = {}'.format(i))
            if left == 0:
                break
        if left <= 0:
            return True
        return False


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

