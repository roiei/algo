

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        dp = [1]*n

        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[j] - arr[i] == difference:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


    def longestSubsequence(self, arr, difference):
        def search(nums, target):
            l = 0
            r = len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return l

        seq = arr[:1]
        for i in range(1, len(arr)):
            if seq[-1] - arr[i] == difference:
                seq += arr[i],
            else:
                pos = search(seq, arr[i])
                print(seq, arr[i], pos)
                if pos >= len(seq):
                    pos = len(seq) - 1
                seq[pos] = arr[i]
        print(len(seq))
        return len(seq)

    def longestSubsequence(self, arr, difference): 
      
        # key = starting element of an AP, 
        # value = length of AP 
        n = len(arr)
        m = dict() 
      
        # since the length of longest AP is at least 
        # one i.e. the number itself. 
        maxt = 1
      
        # if element a[i]'s starting element(i.e., a[i]-i*d) 
        # is not in map then its value is 1 else there already 
        # exists a starting element of an AP of which a[i] 
        # can be a part. 
        for i in range(n): 
            if (arr[i] - i * difference) in m: 
                m[arr[i] - i * difference] += 1
            else: 
                m[arr[i] - i * difference] = 1
      
        # In this it variable will be 
        # storing key value of dictionary. 
        for it in m: 
            if m[it] > maxt: 
      
                # calculating the length of longest AP. 
                maxt = m[it] 
      
        print(maxt)
        return maxt 
        

print(4 == Solution().longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))

#print(Solution().longestSubsequence([3,4,-3,-2,-4], -5))
#print(Solution().longestSubsequence([3,0,-3,4,-4,7,6], 3))


