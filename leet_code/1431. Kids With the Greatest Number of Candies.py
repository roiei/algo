class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for candy in candies:
            res += True if candy + extraCandies >= mx else False

        return res
