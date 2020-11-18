import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


"""
You are given an array of network towers towers and an integer radius, 
where towers[i] = [xi, yi, qi] denotes the ith network tower with location (xi, yi) 
and quality factor qi. 
All the coordinates are integral coordinates on the X-Y plane,
 and the distance between two coordinates is the Euclidean distance.

The integer radius denotes the maximum distance in which 
the tower is reachable. 
The tower is reachable if the distance is less than or equal to radius. 

Outside that distance, the signal becomes garbled, and the tower is not reachable.

The signal quality of the ith tower at a coordinate (x, y) 
is calculated with the formula 

        ⌊qi / (1 + d)⌋, 

where d is the distance between the tower and the coordinate. 
The network quality at a coordinate is the sum of the signal qualities 
from all the reachable towers.


Return the integral coordinate where the network quality is maximum. 
If there are multiple coordinates with the same network quality, 
return the lexicographically minimum coordinate.


Note:

A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either x1 < x2 or x1 == x2 and y1 < y2.
⌊val⌋ is the greatest integer less than or equal to val (the floor function).

"""

class Solution:
    def bestCoordinate(self, towers: [[int]], radius: int) -> [int]:
        


stime = time.time()
print([2,1] == Solution().bestCoordinate(towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2))
print('elapse time: {} sec'.format(time.time() - stime))


