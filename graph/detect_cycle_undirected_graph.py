"""
Problem Description

Given an undirected graph having A nodes labelled from 1 to A with M edges given in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents two nodes B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""

class Solution:
    def dfs(self, vertex, adjacency_list, visited, parent):
        visited.add(vertex)
        if vertex in adjacency_list:
            for neighbour in adjacency_list[vertex]:
                if neighbour not in visited:
                    if self.dfs(neighbour, adjacency_list, visited, vertex):
                        return True
                elif neighbour!=parent:
                    return True

        return False # No cycle

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # build the adjacency list first 
        adjacency_list = {}
        for x in B:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append(x[1])
            else:
                adjacency_list[x[0]] = [x[1]]
        
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append(x[0])
            else:
                adjacency_list[x[1]] = [x[0]]

        visited = set()
        for v in range(1, A+1):
            if v in visited:
                continue
            if self.dfs(v, adjacency_list, visited, -1):
                return 1
        
        return 0