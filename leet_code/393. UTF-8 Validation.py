import time
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        nums = data
        while nums:
            num = nums.pop(0)
            num = '{:08b}'.format(num)
            byte_cnt = 0
            for i in range(4):
                if 1 == int(num[i]):
                    byte_cnt += 1
                if 0 == int(num[i]):
                    break

            if byte_cnt == 0:
                continue

            if byte_cnt == 1:
                return False
            elif byte_cnt >= 2:
                if int(num[byte_cnt]) != 0:
                    return False

            byte_cnt -= 1
            while nums and (byte_cnt) > 0:
                fnum = nums.pop(0)
                fnum = '{:08b}'.format(fnum)
                if not (int(fnum[0]) == 1 and int(fnum[1]) == 0):
                    return False
                byte_cnt -= 1

            if byte_cnt != 0:
                return False

        return True

    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return False

        while data:
            num = data.pop(0)
            num = '{:08b}'.format(num)
            ones = 0
            for i in range(5):
                if '0' == num[i]:
                    break
                ones += 1
            
            if not ((2 <= ones <= 4) or ones == 0):
                return False
            
            ones -= 1
            while ones > 0 and data:
                num = data.pop(0)
                num = '{:08b}'.format(num)
                if not (num[0] == '1' and num[1] == '0'):
                    return False
                ones -= 1
                
            if ones > 0:
                return False

        return True


stime = time.time()
print(True == Solution().validUtf8([197, 130, 1]))
print(False == Solution().validUtf8([235, 140, 4]))
print('elapse time: {} sec'.format(time.time() - stime))