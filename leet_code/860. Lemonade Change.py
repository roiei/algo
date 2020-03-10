class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return False
        changes = [0]*2
        cost = {}
        cost[0] = 10
        cost[1] = 5
        
        for bill in bills:
            left = bill - 5
            if bill == 5:
                changes[1] += 1
            elif bill == 10:
                changes[0] += 1
            
            if 0 == left:
                continue
            
            for i in range(len(changes)):
                while cost[i] <= left and changes[i] > 0:
                    left -= cost[i]
                    changes[i] -= 1
            if left > 0:
                return False
        return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return False
        changes = {5:0, 10:0}
        
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                changes[10] += 1
                if changes[5] < 1:
                    return False                    
                changes[5] -= 1
            elif bill == 20:
                if changes[10] < 1:
                    if changes[5] < 3:
                        return False
                    changes[5] -= 3
                elif changes[10] > 0:
                    changes[10] -= 1
                    if changes[5] < 1:
                        return False
                    changes[5] -= 1
                
        return True
        