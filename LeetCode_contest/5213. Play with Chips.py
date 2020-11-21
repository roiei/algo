

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        kinds = set(chips)
        mn = float('inf')
        
        for kind in kinds:
            cost = 0
            for chip in chips:
                if kind == chip:
                    continue
                diff = abs(kind - chip)
                remain = diff%2
                cost += remain
            mn = min(mn, cost)
        return mn
            