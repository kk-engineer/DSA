"""
Problem Description
There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.
"""

class Solution:

    def isCyclic(self, vertex, visited, recursion_set, adj_list):
        visited.add(vertex)
        recursion_set.add(vertex)

        if vertex in adj_list:
            for neighbour in adj_list[vertex]:
                if neighbour not in visited:
                    if self.isCyclic(neighbour, visited, recursion_set, adj_list):
                        return True
                elif neighbour in recursion_set:
                    return True 
        
        recursion_set.remove(vertex)
        return False

	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer

    def solve(self, A, B, C):
        # if there is a cyclic dependency then we cannot complete all the courses

        # build the adjacency list 
        adj_list = {}
        for i, value in enumerate(B):
            if value in adj_list:
                adj_list[value].append(C[i])
            else:
                adj_list[value] = [C[i]]
        
        visited = set()
        # check for cycle 
        for v in range(1, A+1):
            if v not in visited:
                recursion_set = set()
                if self.isCyclic(v, visited, recursion_set, adj_list):
                    return 0
        
        return 1