

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        mword = ''
        for ch in word:
            if ch.isdigit():
                mword += ch
            else:
                mword += ' '

        mword = mword.strip().split()
        freq = collections.defaultdict(int)
        for word in mword:
            freq[int(word)] += 1

        return len(freq)
