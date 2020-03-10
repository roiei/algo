import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


import threading
from threading import Lock
import time

class Foo:
    def __init__(self):
        self.first_done = Lock()
        self.second_done = Lock()
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.acquire()
        printSecond()
        self.second_done.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.acquire()
        printThird()


stime = time.time()
sol = Foo()
sol.first(lambda:print('first'))
sol.third(lambda:print('third'))
sol.second(lambda:print('second'))
print('o' == sol.decodeAtIndex("leet2code3", 10))
print('elapse time: {} sec'.format(time.time() - stime))
