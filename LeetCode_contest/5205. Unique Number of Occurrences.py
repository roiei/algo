

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.Counter(arr)
        used = []
        for k, v in freq.items():
            if v not in used:
                used += v,
            else:
                return False
        return True

