"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # store all the co-ordinates (as tuples) that have been visited
        visited = set()
        # add the rotten oranges to a Q first
        from collections import deque
        dq = deque([])
        rows, cols = len(A), len(A[0])
        for r in range(rows):
            for c in range(cols):
                if A[r][c]==2:  # rotten
                    curr_co_ord = (r,c)
                    # add to Q
                    dq.append((curr_co_ord, 0))
                    # mark them visited
                    visited.add(curr_co_ord)

        # keep popping the elements in the Q until its empty
        max_minutes = 0
        while dq:
            curr = dq.popleft()
            curr_x, curr_y, curr_mint = curr[0][0], curr[0][1], curr[1]
            max_minutes = max(max_minutes, curr_mint)
            offset_x = [-1, 0, 1, 0]
            offset_y = [0, -1, 0, 1]
            for k in range(4):
                neighbour_x, neighbour_y = curr_x+offset_x[k], curr_y+offset_y[k]
                neighbour_co_ord = (neighbour_x, neighbour_y)
                # check co-ordinates within range, 
                # check not empty cell
                # and  check not visited
                if neighbour_x>=0 and neighbour_x<rows and \
                    neighbour_y>=0 and neighbour_y<cols and \
                    A[neighbour_x][neighbour_y]!=0 and \
                    neighbour_co_ord not in visited: 
                    # add co-ordinates to visited    
                    visited.add(neighbour_co_ord)
                    # add to Q           
                    dq.append((neighbour_co_ord, curr_mint+1))      
        
        # check if all the non-empty cells have been visited
        # else return -1 
        for r in range(rows):
            for c in range(cols):
                curr_co_ord = (r,c)
                if A[r][c]==1 and curr_co_ord not in visited:
                    return -1 
        
        return max_minutes