
class Solution:

    def __init__(self, nums: List[int]):
        self.vals = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.vals[num] += i,

    def pick(self, target: int) -> int:
        if target not in self.vals:
            return -1
        n = len(self.vals[target])
        idx = random.randint(0, n-1)
        return self.vals[target][idx]