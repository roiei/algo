


class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        q = [i for i in range(10)]
        res = []

        while q:
            num = q.pop(0)
            if low <= num <= high:
                res += num,

            if num == 0 or num > high:
                continue

            lms_digit = num%10
            lower_num = num*10 + (lms_digit - 1)
            higher_num = num*10 + (lms_digit + 1)

            if lms_digit == 0:
                q += higher_num,
            elif lms_digit == 9:
                q += lower_num,
            else:
                q += lower_num,
                q += higher_num,
        
        return sorted(res)
  

print([0,1,2,3,4,5,6,7,8,9,10,12,21] == Solution().countSteppingNumbers(low = 0, high = 21))
#print(True == Solution().isValidPalindrome('abcdeca', 2)) # removing b anc e