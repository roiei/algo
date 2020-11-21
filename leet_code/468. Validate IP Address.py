
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def validIPAddress(self, IP: str) -> str:
        chunks = []
        ip_type = 'IPv4'
        num_chunks = 4
        
        if IP.find('.') != -1:
            chunks = IP.split('.')
        else:
            chunks = IP.split(':')
            num_chunks = 8
            ip_type = 'IPv6'

        if num_chunks != len(chunks):
            return 'Neither'
        
        if ip_type == 'IPv4':
            for chunk in chunks:
                if not chunk:
                    return 'Neither'

                try:
                    num = int(chunk)
                except ValueError:
                    return 'Neither'

                if str(num) != chunk:
                    return 'Neither'
                
                if not (0 <= num <= 255):
                    return 'Neither'
        else:
            for chunk in chunks:
                if not chunk:
                    return 'Neither'
                
                for ch in chunk.lower():
                    if not ('0' <= ch <= '9' or 'a' <= ch <= 'f'):
                        return 'Neither'
                
                if len(chunk) > 4:
                    return 'Neither'
        
        return ip_type
        

stime = time.time()
print("Neither" == Solution().validIPAddress("00.0.0.0"))
#print("Neither" == Solution().validIPAddress("256.256.256.256"))
#print("IPv4" == Solution().validIPAddress("172.16.254.1"))
# print("IPv6" == Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print("Neither" == Solution().validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))
# print("Neither" == Solution().validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))
#print("Neither" == Solution().validIPAddress("15.16.-0.1"))
# print("Neither" == Solution().validIPAddress("1e1.4.5.6"))
# print("IPv4" == Solution().validIPAddress("192.0.0.1"))
# print("IPv4" == Solution().validIPAddress("172.16.254.1"))
print('elapse time: {} sec'.format(time.time() - stime))