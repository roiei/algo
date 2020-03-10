class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n = '{:08b}'.format(N)
        idx = n.find('1')
        n = n[idx:]
        n = ['1' if i == '0' else '0' for i in n]
        n = int('0b' + ''.join(n), 2)
        return n
