class Solution:
    def distributeCandies(self, candies) -> int:
        if not candies:
            return 0
        n = len(candies)//2
        k = 0
        candies.sort()
        pre = -1
        for candy in candies:
            if pre != candy:
                k += 1
                pre = candy
        return k if k <= n else n
