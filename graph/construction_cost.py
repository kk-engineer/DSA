"""
Problem Description
Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.

Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.

NOTE: Return the answer modulo 109+7 as the answer can be large.
"""

import heapq 

# Prims' Algorithm 
# BFS

class Solution:

    def get_adj_list(self, adj_matrix):
        adj_list = {}
        for x in adj_matrix:
            if x[0] in adj_list:
                adj_list[x[0]].append((x[1], x[2]))
            else:
                adj_list[x[0]] = [(x[1], x[2])]
            
            # add the reverse edges too, since un-directed
            if  x[1] in adj_list:
                adj_list[x[1]].append((x[0], x[2]))
            else:
                adj_list[x[1]] = [(x[0], x[2])]

        return adj_list

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # build adjacency list first 
        adj_list = self.get_adj_list(B)

        # visited vertices set 
        visited = set()

        # min heap to get the least wt vertex next 
        min_heap = []
        # insert the 1st node with wt=0 first in the min heap and start 
        heapq.heappush(min_heap, (0, 1))

        min_cost = 0

        while min_heap:
            # pop the min wt vertex 
            curr = heapq.heappop(min_heap)
            curr_wt, curr_v = curr[0], curr[1]

            # check if the vertex is not visited and then proceed 
            if curr_v not in visited:
                # mark the current vertex as visited
                visited.add(curr_v)
                # add the current wt to min cost 
                min_cost+=curr_wt

                # check if the curr vertex has entry in adjacency list 
                if curr_v in adj_list:
                    # check all its neighbours 
                    for nbr in adj_list[curr_v]:
                        nbr_wt, nbr_v = nbr[1], nbr[0]
                        # if neighbour is not visited only then add it to the heap 
                        if nbr_v not in visited:
                            heapq.heappush(min_heap, (nbr_wt, nbr_v))
        
        return min_cost%(10**9 + 7)