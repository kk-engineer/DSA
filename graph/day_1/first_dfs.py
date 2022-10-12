"""
Problem Description
You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

B C : query to find whether B is reachable from C.

Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.
"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer

    def solve(self, A, B, C):
        n = len(A)
        adjacency_list = {}
        for i in range(1, n):
            if A[i] in adjacency_list:
                adjacency_list[A[i]].append(i+1)
            else:
                adjacency_list[A[i]] = [i+1]
        
        # check if there is a path from C to B
        stack = []
        stack.append(C)
        while stack:
            curr = stack.pop()
            if curr==B:
                return 1
            if curr in adjacency_list:
                stack.extend(adjacency_list[curr])

        return 0