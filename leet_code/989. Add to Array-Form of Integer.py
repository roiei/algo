

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(map(int, list(str(int(''.join([str(v) for v in A])) + K))))
        
