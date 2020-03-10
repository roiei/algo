class Solution:
    def reverseBits(self, n):
        return int('0b'+'{:032b}'.format(n)[::-1], 2)
