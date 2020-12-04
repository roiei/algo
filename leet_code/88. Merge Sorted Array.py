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

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        i = len(nums1) - 1

        while i1 >= 0 or i2 >= 0:
            if i1 >= 0 and i2 >= 0:
                if nums1[i1] > nums2[i2]:
                    nums1[i] = nums1[i1]
                    i1 -= 1
                    i -= 1
                else:
                    nums1[i] = nums2[i2]
                    i2 -= 1
                    i -= 1
            elif i1 >= 0:
                nums1[i] = nums1[i1]
                i1 -= 1
                i -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
                i -= 1

        return nums1 # just for validation


print([1] == Solution().merge([0], 0, [1], 1))
#print([1,2,2,3,5,6] == Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

