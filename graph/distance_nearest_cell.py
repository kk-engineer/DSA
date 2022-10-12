"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows, cols = len(A), len(A[0])
        # create ans matrix of same dimensions as A and initialise it with 0 
        ans = [[0]*(cols) for _ in range(rows)]

        from collections import deque 
        dq = deque([])
        visited = set()
        # first add all the 1's to the Q with distance 0
        for r in range(rows):
            for c in range(cols):
                if A[r][c]==1:
                    dq.append(((r,c), 0))
                    visited.add((r,c))
        
        # keep going until the Q is empty
        while dq:
            curr = dq.popleft()
            curr_co_ord, curr_dist = curr[0], curr[1]
            x_offset = [-1, 0, 1, 0]
            y_offset = [0, -1, 0, 1]
            for k in range(4):
                # neighbour cell 
                neighbour_co_ord = (curr_co_ord[0]+x_offset[k], curr_co_ord[1]+y_offset[k])
                # check if the neighbour cell is within matrix boundaries 
                if neighbour_co_ord[0]>=0 and neighbour_co_ord[0]<rows and \
                    neighbour_co_ord[1]>=0 and neighbour_co_ord[1]<cols and \
                    A[neighbour_co_ord[0]][neighbour_co_ord[1]]!=1 and \
                    neighbour_co_ord not in visited:
                    # add to visited 
                    visited.add(neighbour_co_ord)
                    # update ans matrix with distance, 
                    # |x1-x2|+|y1-y2| will be +1 for all 4 neighbours
                    ans[neighbour_co_ord[0]][neighbour_co_ord[1]] = curr_dist+1
                    # add to Q
                    dq.append((neighbour_co_ord, curr_dist+1))
        
        return ans