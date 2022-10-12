"""
Problem Description
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def lis(self, A):
        # max_len is the longest increasing sub-sequence length
        max_len, n = 1, len(A)
        # initialise the LIS list with 1 , since the min LIS will be 1
        LIS = [1]*n

        # iterate from 1 to n-1, since the LIS for first element will always be 1
        for i in range(1, n):
            curr_max = 0
            # check for the LIS of A[j] before index i, that is less than A[i]
            # get the max LIS value for numbers less than A[i]
            for j in range(i):
                if A[j]<A[i]:
                    curr_max = max(curr_max, LIS[j])
            # add 1 to the max LIS value received, 
            # since 1 more element can be added that is the current index element 
            LIS[i]=curr_max+1
            # update the max_len with max length found till now 
            max_len = max(max_len, LIS[i])
        
        return max_len
