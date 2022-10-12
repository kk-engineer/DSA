"""
Problem Description
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
"""

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        rows, cols = len(A), len(A[0])
        # check if the ball can stop at destination
        # right , left, up , down
        xOff = [1, -1, 0, 0]
        yOff = [0, 0, 1, -1]
        
        from collections import deque
        dq = deque([])
        start, end = tuple(B), tuple(C)
        visited = set()
        # add the start node with distance=0
        dq.append((start,0))
        # mark visited
        # keep a separate visited set to mark positions as visited
        # do not mark the position=1 in the matrix, as this will alter the matrix 
        # and show blocked positions which are not there, i.e marked as blocked by us 
        visited.add(start)
       
       # Do a BFS , keep going while the DQ is not empty 
        while dq:
            curr = dq.popleft()
            
            # check if the current position is same as destination
            # return the distance
            if curr[0]==end:
                return curr[1]
            
            for i in range(4):
                next_pos_x = curr[0][0]+xOff[i]
                next_pos_y = curr[0][1]+yOff[i]
                # increase the distance by 1 as the x,y co-ordinates have been offset by 1
                curr_dist = curr[1]+1
                # go until the ball hits a dead end
                while next_pos_x>=0 and next_pos_x<rows and \
                    next_pos_y>=0 and next_pos_y<cols and \
                    A[next_pos_x][next_pos_y]==0:
                    next_pos_x+=xOff[i]
                    next_pos_y+=yOff[i]
                    curr_dist+=1
                
                # mark the position before dead end as visited and 
                # add it to the DQ 
                next_pos_x-=xOff[i]
                next_pos_y-=yOff[i]
                next_pos = (next_pos_x, next_pos_y)
                curr_dist-=1
                # check if already visited
                if next_pos not in visited:
                    # mark visited
                    visited.add(next_pos)
                    # add to DQ
                    dq.append((next_pos, curr_dist))

        return -1