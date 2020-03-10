import time


class Solution:
    def maxProduct(self, words: 'List[str]') -> int:
        uniques = [set(word) for word in words]
        n = len(uniques)
        m_len = 0
        for i in range(n):
            for j in range(n):
                if uniques[i] & uniques[j]:
                    continue
                m_len = max(m_len, len(words[i])*len(words[j]))
        return m_len


stime = time.time()
print(Solution().maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
print('elapse time: {} sec'.format(time.time() - stime))
