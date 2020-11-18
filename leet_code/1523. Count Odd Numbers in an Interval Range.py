class Solution:
    def countOdds(self, low: int, high: int) -> int:
        while low < high and low%2 == 0:
            low += 1

        while high%2 != 0:
            high += 1

        return (high - low + 1)//2