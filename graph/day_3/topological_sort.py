"""
Problem Description
Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Return the topological ordering of the graph and if it doesn't exist then return an empty array.

If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

NOTE:

There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""

import sys 
import heapq

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        # an array to store the indegree of each vertex 
        indegree_map = [0]*(A+1)

        # build the adjacency list and update the indegree map
        adjacency_list = {}
        for x in B:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append(x[1])
            else:
                adjacency_list[x[0]] = [x[1]]

            indegree_map[x[1]]+=1

        # min heap to store the vertices in lexographically sorted order 
        min_heap = []
        # push all the vertices with indegree==0 to the min heap 
        for i in range(1, A+1):
            if indegree_map[i]==0:
                heapq.heappush(min_heap, i)

        ans = []
        # loop until the min heap is not empty 
        while min_heap:
            # pop the current min 
            curr = heapq.heappop(min_heap)
            # add it to our ans array 
            ans.append(curr)
            # check if the curr vertex is present in our adjacency_list
            if curr in adjacency_list:
                # iterate through all its neighbours - BFS 
                for neighbour in adjacency_list[curr]: 
                    # if indegree of neighbour>0, means still there are unresolved dependencies
                    if indegree_map[neighbour]>0:
                        # reduce the dependency/indegree by 1
                        indegree_map[neighbour]-=1
                        # if the indegree of neighbour==0 , add to min heap 
                        if indegree_map[neighbour]==0:
                            heapq.heappush(min_heap, neighbour)
        
        return ans