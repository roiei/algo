

class Solution:
    def get_alphabet(self, num, idx):
        convert_tbl = [
            ['A', 'B', 'C'], 
            ['D', 'E', 'F'],
            ['G', 'H', 'I'],
            ['J', 'K', 'L'],
            ['M', 'N', 'O'],
            ['P', 'R', 'S'],
            ['T', 'U', 'V'],
            ['W', 'X', 'Y']
        ]
        if num-2 < 0 or num-2 >= len(convert_tbl) or idx >= 3 or idx < 0:
            return '1' if num is 1 else '2' if num is 2 else '.'
        return convert_tbl[num-2][idx]

    def combinate_tel_nums(self, nums, cur, trace):
        if cur == len(nums):
            print(''.join(trace))
            return
        n = len(nums)
        for i in range(3):
            trace.append(self.get_alphabet(nums[cur], i))
            self.combinate_tel_nums(nums, cur+1, trace)
            trace.pop()

num = [4, 9, 7, 1, 9, 2, 7]

sol = Solution()
print(sol.combinate_tel_nums(num, 0, []))

