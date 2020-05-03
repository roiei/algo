
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def entityParser(self, text: str) -> str:
        entities = {'&quot;':'\"', '&apos;':'\'', '&amp;':'&', '&gt;':'>', '&lt;':'<', '&frasl;':'/'}
        for entity in entities:
            text = text.replace(entity, entities[entity])
        return text


stime = time.time()
print("& is an HTML entity but &ambassador; is not." == Solution().entityParser(text = "&amp; is an HTML entity but &ambassador; is not."))
print('elapse time: {} sec'.format(time.time() - stime))