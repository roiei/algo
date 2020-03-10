class Solution:
    def numRabbits_es(self, answers: 'List[int]') -> int:
        cnt = 0
        while answers:
            cur = answers.pop()
            cnt += 1
            if 0 == cur:
                continue
            for j in range(cur):
                if cur in answers:
                    answers.remove(cur)
                cnt+= 1
        return cnt

    def numRabbits(self, answers: 'List[int]') -> int:
        cnt = 0
        kind = {}
        for val in answers:
            if 0 == val:
                cnt+= 1
            elif val not in kind:
                kind[val] = 1
            else:
                kind[val]+= 1
        for val, num in kind.items():
            unit = val+1
            while num >= unit:
                num-= unit
                cnt+= unit
            if num > 0:
                cnt+= unit
        return cnt

answers = [1, 1, 2] # 5
answers = [1,0,1,0,0] # 5
answers = [0,0,1,1,1] # 6
stime = time.time()
sol = Solution()
print(sol.numRabbits(answers)) # 0
print('elapse time: {} sec'.format(time.time() - stime))