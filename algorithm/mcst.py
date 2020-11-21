
import time
import heapq
import copy
import collections
import operator


def minnode(n, keyval, mcst_set): 
    mini = float('inf')
    mini_index = None
      
    # find min cost node
    for i in range(n): 
        if i in mcst_set:
            continue

        if keyval[i] < mini:
            mini = keyval[i] 
            mini_index = i 

    return mini_index 


# Function to find out the MST and  
# the cost of the MST.  
def findcost(n, city): 
    path = collections.defaultdict(int)
      
    # Array to store key value  
    # of each node.  
    keyval = [float('inf')] * n  
      
    # Boolean Array to hold bool  
    # values whether a node is 
    # included in MST or not.  

    non_visited = [i for i in range(1, n)]
    mcst_set = set()
      
    # Start to find the MST from node 0.  
    # minimum cost to reach 0th node from 0th node is 0.  
    keyval[0] = 0
      
    # Find the rest n-1 nodes of MST. 
    for i in range(n - 1): 
      
        # First find out the minimum node which is not yet included in the MCST
        u = minnode(n, keyval, mcst_set)  
        mcst_set.add(u)
      
        # Update the values of neighbor  
        # nodes of u which are not yet  
        # included in MST.  
        for v in range(n):
            if v in mcst_set:
                continue

            if city[u][v] and city[u][v] < keyval[v]:
                keyval[v] = city[u][v]  
                path[v] = u
      
    # Find out the cost by adding  
    # the edge values of MST.  
    cost = 0
    for i in range(1, n): 
        cost += city[path[i]][i]
    print(cost)
    return cost


# Driver Code 
if __name__ == '__main__': 
  
    # Input 1  
    n1 = 5
    city1 = [[0, 1, 2, 3, 4],  
             [1, 0, 5, 0, 7],  
             [2, 5, 0, 6, 0], 
             [3, 0, 6, 0, 0],  
             [4, 7, 0, 0, 0]]  
    print(10 == findcost(n1, city1))
      
    # Input 2  
    n2 = 6
    city2 = [[0, 1, 1, 100, 0, 0], 
             [1, 0, 1, 0, 0, 0],  
             [1, 1, 0, 0, 0, 0],  
             [100, 0, 0, 0, 2, 2], 
             [0, 0, 0, 2, 0, 2],  
             [0, 0, 0, 2, 2, 0]]  
    print(106 == findcost(n2, city2))
