"""
Problem Description
Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

=> D[i] : Shortest distance form the C node to node i.

=> If node i is not reachable from C then -1.

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
"""

import sys
import heapq

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        # build the adjacency list 
        adjacency_list = {}
        for x in B:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append((x[1], x[2]))
            else:
                adjacency_list[x[0]] = [(x[1], x[2])]
            # need to add both the edges , since undirected graph 
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append((x[0], x[2]))
            else:
                adjacency_list[x[1]] = [(x[0], x[2])]
            
        # create a distance array with all the distances initialised with Infinity  
        distance = [sys.maxsize]*A 
        # min heap to store all the distance, vertices
        # the priority will be decided based on distance from Source
        min_heap = []
        # push the source node with distance 0 into the node 
        heapq.heappush(min_heap, (0, C))
        # initialise the distance of source node with 0
        distance[C] = 0 

        while min_heap:
            # pop the current min distance vertex from source 
            curr = heapq.heappop(min_heap)
            curr_distance = curr[0]
            curr_vertex = curr[1]
            # iterate through all its neighbours
            if curr_vertex in adjacency_list:
                for neighbour in adjacency_list[curr_vertex]:
                    curr_nbr = neighbour[0]
                    curr_nbr_distance = curr_distance + neighbour[1]
                    # if the distance to current neighbour from Source is less than the previous distance
                    # update the distance array and push the vertex in min heap 
                    if curr_nbr_distance<distance[curr_nbr]:
                        distance[curr_nbr] = curr_nbr_distance
                        heapq.heappush(min_heap, (curr_nbr_distance, curr_nbr))
        
        # if the distance of a vertex from Source is infifinity, mark it as -1 
        for i in range(A):
            if distance[i]==sys.maxsize:
                distance[i]=-1

        return distance