"""
Problem Description
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.
"""

import heapq 

# Minimal Spanning Tree
# BFS 
# Prim's Algorithm 

class Solution:
    def get_adjacency_list(self, adjacency_matrix):
        adjacency_list = {}

        for x in adjacency_matrix:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append((x[1], x[2]))
            else:
                adjacency_list[x[0]] = [(x[1], x[2])]
            
            # add the reverse edge too, since undirected 
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append((x[0], x[2]))
            else:
                adjacency_list[x[1]] = [(x[0], x[2])]

        return adjacency_list

	# @param A : integer
	# @param B : list of list of integers
	# @return an integer

    def solve(self, A, B):
        adjacency_list = self.get_adjacency_list(B)

        # visited vertices set 
        visited = set()

        # build a priority Q 
        min_heap = []
        # add the vertex 1 (any vertex can be choses) , and its wt 0 to the min heap to start 
        heapq.heappush(min_heap, (0, 1))

        min_cost = 0
        while min_heap:
            # pop the current min wt vertex from min heap 
            curr = heapq.heappop(min_heap)
            curr_wt, curr_vertex = curr[0], curr[1]
            # add the current vertex to visited , if not visited 
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                # add the curr vertex wt to min cost 
                min_cost+=curr_wt

                # check if current vertex is in adjacency_list
                if curr_vertex in adjacency_list:
                    # check all its nighbours
                    for neighbour in adjacency_list[curr_vertex]:
                        curr_nbr = neighbour[0]
                        nbr_wt = neighbour[1]
                        # if the neighbour is not visited add it to min heap with its wt
                        if curr_nbr not in visited:
                            heapq.heappush(min_heap, (nbr_wt, curr_nbr))


        return min_cost