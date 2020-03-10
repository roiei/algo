import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import re


class Solution:
    def simplifyPath_old(self, path: str) -> str:
        path = re.sub('[.]{3}[^a-zA-Z]*$', '@', path)
        #path = re.sub('\.\.hidden', '&', path)
        #path = re.sub('\.hidden', '$', path)
        path = re.sub('[.]{2}[^a-zA-Z]*$', '#', path)
        path = re.sub('[.][^a-zA-Z]*$', '', path)
        path = re.sub('[#]', '..', path)
        path = re.sub('[/]+', '/', path)
        path = path.replace('/./', '/')
        path = re.sub('[@]', '...', path)
        #path = re.sub('[$]', '.hidden', path)
        #path = re.sub('[&]', '..hidden', path)
        path = path.split('/')
        stk = []
        while path:
            val = path.pop(0)
            if stk and '..' == val:
                stk.pop()
                continue
            if '' == val or '..' == val:
                continue
            stk += val,
        return '/' + '/'.join(stk)


    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = [p for p in path if '' != p]
        stk = []
        while path:
            val = path.pop(0)
            if stk and '..' == val:
                stk.pop()
                continue
            if '.' == val or '..' == val:
                continue
            stk += val,
        return '/' + '/'.join(stk)


stime = time.time()
print('/home/foo' == Solution().simplifyPath("/home//foo/"))
# print('/c' == Solution().simplifyPath("/a/./b/../../c/"))
# print('/c' == Solution().simplifyPath("/a/../../b/../c//.//"))
# print("/a/b/c" == Solution().simplifyPath("/a//b////c/d//././/.."))
# print("/a/b/c" == Solution().simplifyPath("/a//b////c/d//././/.."))
# print("/..." == Solution().simplifyPath("/..."))
# print("/.hidden" == Solution().simplifyPath("/.hidden"))
# print("/..hidden" == Solution().simplifyPath("/..hidden"))
# print("/.aa/....hidden" == Solution().simplifyPath("/.aa/....hidden"))
print('elapse time: {} sec'.format(time.time() - stime))