"""
Problem Description
Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).

If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.

Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.

If there is no possible path from vertex i to vertex j , B[i][j] = -1

Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        # n = no. of vertices 
        n = len(A)

        for v in range(n):
            for r in range(n):
                if A[r][v]!=-1:
                    for c in range(n):
                        if r!=c and A[v][c]!=-1:
                            temp = A[r][v]+A[v][c]
                            if A[r][c]==-1 or A[r][c]>temp:
                                A[r][c]=temp
        return A