class Solution:
    def validUtf8(self, data: 'List[int]') -> 'bool':
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


data = [197, 130, 1]
data = [240, 162, 138, 147, 17]
data = [248, 130, 130, 130]

sol = Solution()
ret = sol.validUtf8(data)
print(ret)