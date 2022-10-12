"""
Problem Description

Given a directed graph with A nodes and M edges.
Find the minimum number of edges that needs to be reversed in order to reach node A from node 1.
"""

import sys 
import heapq 
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def reverseEdges(self, A, B):
        # build the adjacency list first 
        adjacency_list = {}
        for x in B:
            # add the given edge with wt=0
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append((x[1], 0))
            else:
                adjacency_list[x[0]] = [(x[1], 0)]
            
            # add the reverse edge with wt=1 
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append((x[0], 1))
            else:
                adjacency_list[x[1]] = [(x[0], 1)]
        
        # we will check for the minimum wt sum path 
        # this path will give minimum number of reversals 

        # insert the first node in min heap
        min_heap = []
        heapq.heappush(min_heap, (0, 1))

        # distance map to store the min distance of each vertex 
        # initialise all with infinity
        distance_map = [sys.maxsize]*(A+1)

        # initialise first node with 0 
        distance_map[1]=0

        # while the min heap has some element keep going 
        while min_heap:
            # pop the min distance vertex
            curr = heapq.heappop(min_heap)
            curr_distance = curr[0]
            curr_vertex = curr[1]
            # check if its present in adjacency list 
            if curr_vertex in adjacency_list:
                # check distance of each neighbour 
                for neighbour in adjacency_list[curr_vertex]:
                    nbr_distance = neighbour[1]
                    nbr_vertex = neighbour[0]
                    curr_nbr_distance = curr_distance + nbr_distance
                    # if curr nbr distance< distance in map , update the map 
                    # and push the tuple (distance, vertex) to min heap 
                    if curr_nbr_distance < distance_map[nbr_vertex]:
                        distance_map[nbr_vertex] = curr_nbr_distance
                        heapq.heappush(min_heap, (curr_nbr_distance, nbr_vertex))  

        # Finally distance map of Ath veertex will have the answer
        return distance_map[A] if distance_map[A]!=sys.maxsize else -1