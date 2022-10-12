"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
"""

class Solution:
    def is_safe(self, x, y, visited, A):
        if x>=0 and x<len(A) and \
            y>=0 and y<len(A[0]) and \
            (x,y) not in visited:
            return True 
        else:
            return False 

    def dfs(self, x, y, visited, A):
        # co-ordinates of all next neighbour cells
        row = [-1, 0, 1, 0, -1, 1, -1, 1]
        col = [0, -1, 0, 1, 1, 1, -1, -1]
        # add to visited set 
        visited.add((x,y))
        for k in range(8):
            # next cell co-ordinates
            x_next, y_next = x+row[k], y+col[k]
            if self.is_safe(x_next, y_next, visited, A) and \
                A[x_next][y_next]==1:
                self.dfs(x_next, y_next, visited, A)

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        sys.setrecursionlimit(10**6)
        rows, cols = len(A), len(A[0])
        visited = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                # if not visited and cell==1, make dfs call 
                if (r,c) not in visited and A[r][c]==1:
                    self.dfs(r,c, visited, A)
                    count+=1
        
        return count