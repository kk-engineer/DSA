"""
Problem Description
Given an array of strings A of size N, find if the given strings can be chained to form a circle.

A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

NOTE: All strings consist of lower case characters.
"""

class Solution:
    def dfsUtil(self, vertex, visited, adj_list):
        visited.add(vertex)
        if vertex in adj_list:
            for nbr in adj_list[vertex]:
                if nbr not in visited:
                    self.dfsUtil(nbr, visited, adj_list)
        
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        # build the adjacency list first
        adj_list, out_deg, in_deg = {}, {}, {}
        vertex_set = set()

        for x in A:
            if x[0] in adj_list:
                adj_list[x[0]].append(x[-1])
                out_deg[x[0]]+=1
                
            else:
                adj_list[x[0]] = [x[-1]]
                out_deg[x[0]] = 1
            
            if x[-1] in in_deg:
                    in_deg[x[-1]]+=1
            else:
                in_deg[x[-1]]=1
            
            vertex_set.add(x[0])
            vertex_set.add(x[-1])

        # check if out degree and in degree of each vertex is same or not 
        for v in out_deg:
            # check if vertex present in in degree map 
            if v in in_deg: 
                if out_deg[v]!=in_deg[v]:
                    return 0
            else:
                return 0
        
        # visited set 
        visited = set ()
        count=0
        # check for number of connected components
        count=0
        for v in vertex_set:
            if v not in visited:
                self.dfsUtil(v, visited, adj_list)
                count+=1
        
        return 1 if count==1 else 0