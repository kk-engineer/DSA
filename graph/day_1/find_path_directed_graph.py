"""
Problem Description
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node

B[i][0] to node B[i][1].

Find whether a path exists from node 1 to node A.

Return 1 if path exists else return 0.

NOTE:

There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adjacency_list = {}
        # update the adjacency_list
        for edge in B:
            if edge[0] in adjacency_list:
                adjacency_list[edge[0]].append(edge[1])
            else:
                adjacency_list[edge[0]] = [edge[1]]
        
        # keep a set for all the visited nodes 
        visited = set()
        from collections import deque 
        dq = deque([])
        # append node 1 to begin with 
        dq.append(1)
        visited.add(1)
        
        while dq:
            # pop the current element and check whether its present in the adjacency_list
            curr = dq.popleft()
            if curr in adjacency_list:
                # get all the neighbours for current node 
                neighbour_list = adjacency_list[curr]
                # iterate through all neighbours and check whether its node A 
                for neighbour in neighbour_list:
                    if neighbour not in visited:
                        if neighbour==A:
                            return 1
                        # add the next neighbour to set and the visited set 
                        dq.append(neighbour)
                        visited.add(neighbour)

        return 0