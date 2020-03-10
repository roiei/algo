import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def get_line(self, words, maxWidth):
        llen, line = 0, ''
        left = maxWidth
        while words:
            word = words.pop(0)
            if left >= len(word):
                line += word
                llen += len(word)
                left -= len(word)
            else:
                words.insert(0, word)
                break
            if left > 0:
                line += ' '
                llen += 1
                left -= 1
            else:
                break
        return line

    def get_padding_info(self, maxWidth, ss, req_delimeter):
        end_pad_len = 0
        pad_lens = [0]*req_delimeter
        num_ws = maxWidth - sum([len(s) for s in ss])

        if req_delimeter > 0:
            pad_len = num_ws//req_delimeter
            left = num_ws%req_delimeter
            for i in range(len(pad_lens)):
                pad_lens[i] = pad_len
                if left > 0:
                    pad_lens[i] += 1
                    left -= 1
        else:
            end_pad_len = num_ws
        return pad_lens, end_pad_len

    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        res = []
        while words:
            line = self.get_line(words, maxWidth)
            ss = line.split()
            pad_lens, end_pad_len = self.get_padding_info(maxWidth, ss, len(ss)-1)

            new_line = ''
            for i in range(len(ss)):
                new_line += ss[i]
                if i != len(ss)-1:
                    new_line += ' '*pad_lens[i]
            new_line += ' '*end_pad_len
            res += new_line,

        last_line = res[-1]
        last_line = last_line.split()
        line = ''
        for i in range(len(last_line)):
            line += last_line[i]
            if i != len(last_line)-1:
                line += ' '

        line += ' '*(maxWidth-len(line))
        res[-1] = line
        return res


stime = time.time()
print(Solution().fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
#print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
#print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
#print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print('elapse time: {} sec'.format(time.time() - stime))