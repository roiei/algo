class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        idx = len(nums1) - 1

        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] < nums2[j]:
                    nums1[idx] = nums2[j]
                    idx -= 1
                    j -= 1
                elif nums1[i] >= nums2[j]:
                    nums1[idx] = nums1[i]
                    idx -= 1
                    i -= 1
            elif i >= 0:
                nums1[idx] = nums1[i]
                idx -= 1
                i -= 1
            elif j >= 0:
                nums1[idx] = nums2[j]
                idx -= 1
                j -= 1

        return nums1


print(Solution().merge([0], 0, [1], 1))
#print([1,2,2,3,5,6] == Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

