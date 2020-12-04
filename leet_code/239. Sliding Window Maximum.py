import time
import bisect
import heapq


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: int) -> 'List[int]':
        if not nums:
            return []
        n = len(nums)
        out = []
        for i in range(n-k+1):
            out.append(max(nums[i:i+k]))
        return out

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        if not nums or len(nums) < k:
            return None

        wnd = nums[:k]
        sorted_wnd = sorted(nums[:k])
        res = [max(wnd)]
        
        for i in range(k, len(nums)):
            left = wnd.pop(0)
            idx = bisect.bisect_left(sorted_wnd, left)
            sorted_wnd.pop(idx)
            
            wnd += nums[i],
            idx = bisect.bisect_left(sorted_wnd, nums[i])
            sorted_wnd.insert(idx, nums[i])
            res += sorted_wnd[-1],
        
        return res

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        """
            using sorted_wnd + variable wnd
        """
        if not nums or len(nums) < k:
            return None

        wnd = nums[:k]
        q = heapq.heapify(nums[:k])
        res = [max(wnd)]
        
        for i in range(k, len(nums)):
            left = wnd.pop(0)
            idx = bisect.bisect_left(sorted_wnd, left)
            sorted_wnd.pop(idx)
            
            wnd += nums[i],
            idx = bisect.bisect_left(sorted_wnd, nums[i])
            sorted_wnd.insert(idx, nums[i])
            res += sorted_wnd[-1],
        
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            using sorted_wnd + fixed wnd
        """
        if not nums or len(nums) < k:
            return None

        wnd = nums[:k]
        sorted_wnd = sorted(nums[:k])
        res = [max(wnd)]
        wnd += [0]
        rear = 0
        wnd_size = k + 1
        front = k%wnd_size
        
        for i in range(k, len(nums)):
            left = wnd[rear%wnd_size]
            rear = (rear + 1)%wnd_size
            
            idx = bisect.bisect_left(sorted_wnd, left)
            sorted_wnd.pop(idx)
            
            wnd[front%wnd_size] = nums[i]
            front = (front + 1)%wnd_size

            idx = bisect.bisect_left(sorted_wnd, nums[i])
            sorted_wnd.insert(idx, nums[i])
            res += sorted_wnd[-1],
        
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            removed wnd
        """
        if not nums or len(nums) < k:
            return None

        sorted_wnd = sorted(nums[:k])
        res = [max(sorted_wnd)]
        
        for i in range(k, len(nums)):
            left = nums[i - k]
            idx = bisect.bisect_left(sorted_wnd, left)
            sorted_wnd.pop(idx)
            
            idx = bisect.bisect_left(sorted_wnd, nums[i])
            sorted_wnd.insert(idx, nums[i])
            res += sorted_wnd[-1],
        
        return res


stime = time.time()
print([3,3,5,5,6,7] == Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) 
print('elapse time: {} sec'.format(time.time() - stime))

