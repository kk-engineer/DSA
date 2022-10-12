"""
Problem Description
Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""

import sys

class Solution:
    def dfs(self, vertex, visited, adjacency_list, recursion_set):
        # add the vertex to visited and current recursion set
        visited.add(vertex)
        recursion_set.add(vertex)

        # check if the vertex is present in adjacency_list
        if vertex in adjacency_list:
            # iterate through all the neighbours of current vertex 
            for neighbour in adjacency_list[vertex]:
                # if current neighbour has not been visited, then visit it.
                if neighbour not in visited:
                    if self.dfs(neighbour, visited, adjacency_list, recursion_set):
                        return True
                # if the current neighbour is a part of current recursion set, 
                # i.e vertices visited as a part of current DFS 
                # then there is a Cycle
                elif neighbour in recursion_set:
                    return True         # cycle detected
        
        # remove current vertex from recursion_set
        recursion_set.remove(vertex)
        return False                        # NO cycle 

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        sys.setrecursionlimit(10**4)
        # build adjacency_list
        adjacency_list = {}
        for x in B:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append(x[1])
            else:
                adjacency_list[x[0]] = [x[1]]

        # visited set 
        visited = set()
        # iterate thrugh all the vertices and perform DFS for each, 
        # keep marking them visited as we go
        for v in range(1, A+1):
            if v not in visited:
                # a set to track the vertices visited during current recursion
                recursion_set = set()
                if self.dfs(v, visited, adjacency_list, recursion_set):
                    return 1
        
        return 0