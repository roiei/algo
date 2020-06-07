
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Twitter:
    def __init__(self):
        self.g = collections.defaultdict(list)
        self.users = collections.defaultdict(list)
        self.cnt = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId] += (self.cnt, tweetId),
        self.cnt += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = self.users[userId][::]
        
        for v in self.g[userId]:
            res += self.users[v]
        
        return [val for cnt, val in sorted(res, key=lambda p: p[0], reverse=True)][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.g[followerId] and followerId != followeeId:
            self.g[followerId] += followeeId,
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.g[followerId]:
            idx = self.g[followerId].index(followeeId)
            self.g[followerId].pop(idx)


