"""
0-1 Knapsack problem 
Problem Description
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE: You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # no. of cols = total weight
        rows, cols = len(A), sum(A)+1
        prev_row_values = [sys.maxsize]*(cols+1)
        prev_row_values[0]=0

        for r in range (1, rows+1):
            # re-initialize current row values with 0
            curr_row_values = [sys.maxsize]*(cols+1)
            curr_row_values[0]=0
            for c in range(1, cols+1):
                curr_excl = prev_row_values[c]
                # check if the current weight is greater than the wt of current index
                curr_incl = prev_row_values[c-A[r-1]] + B[r-1]    # add the current wt B[r-1]

                curr_row_values[c] = min(curr_excl, curr_incl)

            # keep a copy of current row in previous row
            prev_row_values = curr_row_values.copy()

        for x in range(cols-1, -1, -1):
            if prev_row_values[x]<=C:
                return x
