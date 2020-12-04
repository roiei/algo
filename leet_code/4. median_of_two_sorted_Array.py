

class Solution:
    def merge(self, num1, num2):
        res = []
        while num1 or num2:
            if num1 and num2:
                if num1[0] < num2[0]:
                    res.append(num1[0])
                    num1.pop(0)
                else:
                    res.append(num2[0])
                    num2.pop(0)
            elif not num1 and num2:
                res.append(num2[0])
                num2.pop(0)
            elif num1 and not num2:
                res.append(num1[0])
                num1.pop(0)
        return res

    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        merged = self.merge(nums1, nums2)
        n = len(merged)
        med = 0
        if n % 2 != 0:
            med = merged[n//2]
        else:
            med = (merged[n//2] + merged[n//2 - 1])/2
        return med

    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        i = j = 0
        nums = []
        
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums += nums1[i],
                    i += 1
                else:
                    nums += nums2[j],
                    j += 1
            elif i < len(nums1) and j == len(nums2):
                nums += nums1[i],
                i += 1
            elif i == len(nums1) and j < len(nums2):
                nums += nums2[j],
                j += 1
        
        if len(nums)%2 == 0:
            return float(nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
        return float(nums[len(nums)//2])


# nums1 = [1, 3]
# nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))