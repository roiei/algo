
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


from threading import Thread
from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_odd = Lock()
        self.lock_even = Lock()
        self.lock_zero = Lock()
        self.lock_odd.acquire()
        self.lock_even.acquire()    
        self.is_odd = True
                
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lock_zero.acquire()
            printNumber(0)
        
            if self.is_odd:
                self.lock_odd.release()
            else:
                self.lock_even.release()
            self.is_odd = not self.is_odd

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        val = 2
        while val <= self.n:
            self.lock_even.acquire()
            printNumber(val)
            val += 2
            self.lock_zero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        val = 1
        while val <= self.n:
            self.lock_odd.acquire()
            printNumber(val)
            val += 2
            self.lock_zero.release()

