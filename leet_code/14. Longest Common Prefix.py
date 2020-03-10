

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''
        s_idx = -1
        s_len = float('inf')
        for i in range(len(strs)):
            if s_len > len(strs[i]):
                s_len = len(strs[i])
                s_idx = i

        compare_set = strs[:s_idx]

        if s_idx+1 < len(strs):
            compare_set += strs[s_idx+1:]
        s_str = strs[s_idx]
        c_seq = ''

        while s_str:
            ncs = []
            common_exist = True
            for word in compare_set:
                found = False
                while word:
                    if word[0] != s_str[0]:
                        break
                    word = word[1:]
                    found = True
                    break
                ncs.append(word)
                if False == found:
                    common_exist = False
                    break
            compare_set = ncs
            if False == common_exist:
                break
            c_seq += s_str[0] 
            s_str = s_str[1:]
        return c_seq


strs = ["dog","racecar","car"] # ''
strs = [""]
strs = ["flow", "ofl", "iflg"] # fl
strs = ["flower","flow","flight"]   # 'f1'
#strs = ["aa","ab"] # a
strs = ["aa","aa"]

sol = Solution()
print(sol.longestCommonPrefix(strs))