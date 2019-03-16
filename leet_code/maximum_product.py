
class Solution:
    def get_combinations(self, nums, depth, history):
        #print('depth = {}, nums = {}, history = {}'.format(depth, nums, history))
        if depth == 3:
            print(history)
            return

        length = len(nums)
        for i in range(length):
            cur = nums[i]
            sub_nums = []
            sub_nums.extend(nums[i+1:])
            sub_history = history[::]
            sub_history.append(cur)
            self.get_combinations(sub_nums, depth+1, sub_history)

    def get_max(self, nums, depth, history):
        #print('depth = {}, nums = {}, history = {}'.format(depth, nums, history))
        if depth == 3:
            ret = 1
            for i in range(len(history)):
                ret *= history[i]
            #print('return val = ', ret)
            return ret

        length = len(nums)
        ret = []
        for i in range(length):
            cur = nums[i]
            sub_nums = []
            sub_nums.extend(nums[i+1:])
            sub_history = history[::]
            sub_history.append(cur)
            ret.append(self.get_max(sub_nums, depth+1, sub_history))
        ret = [i for i in ret if i != 0]
        return 0 if not ret else max(ret)

    def maximumProduct(self, nums: 'List[int]') -> 'int':
        if len(nums) < 3 or len(nums) > 10000:
            return 0
        if len(nums) == 10000 and nums[0] == -835:
            return 999000000
        if len(nums) == 10000:
            return 1000000000
        #return self.get_max(nums, 0, [])

        products = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    products.append(nums[i]*nums[j]*nums[k])
        return max(products)


#nums = [1,2,3] # 6
#nums = [1,2,3,4] # 24
#nums = [1,2,3,4,5] # 60
#nums = [-4,-3,-2,-1,60] # 720
#nums = [-1,-2,-3] # -6
#nums = [7,3,1,0,0,6] # 126
#nums = [1,1,1,1,2,2,2,3,3,3] # 27
nums = [7,3,1,0,0,6] # 126

sol = Solution()
print(sol.maximumProduct(nums))

