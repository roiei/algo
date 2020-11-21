class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = len(nums1) - 1
        i = m - 1
        j = n - 1
        
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0 and nums1[i] < nums2[j]:
                nums1[tail] = nums2[j]
                j -= 1
                tail -= 1
            elif (i >= 0 and j >= 0) or (i >= 0 and j == 0):
                nums1[tail] = nums1[i]
                i -= 1
                tail -= 1
            else:
                print(tail, j)
                nums1[tail] = nums2[j]
                j -= 1
                tail -= 1

        return nums1


print([1,2,2,3,5,6] == Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6],       n = 3))
        