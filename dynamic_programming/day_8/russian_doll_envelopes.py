"""
Problem Description

Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.

One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

Find the maximum number of envelopes you can put one inside other.
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # create a list of tuples from the given input matrix of ht and width 
        n = len(A)
        # list of ht, wd tuples
        ht_wd_list = []
        for x in A:
            ht_wd_list.append((x[0], x[1]))

        # sort the list of tuples, based on ht, i.e, first element, i.e height
        ht_wd_list.sort()
        # initialise the max_envlp_count list with default value 1, i.e, min count of envelopes possible
        max_envlp_count=[1]*n
        # maximum possible count and our answer
        max_count = 1

        # iterate through all the ht, wd tuples,
        # since they are sorted by ht we only need to consider the widths
        for i in range(1, n):
            curr_max = 0
            # check for each width before ith index
            for j in range(i):
                # if current width is less than the width at ith index,
                # check only if the height are not same
                if ht_wd_list[j][0]!=ht_wd_list[i][0] and \
                    ht_wd_list[j][1]<ht_wd_list[i][1]:      # width[j]<width[i]
                    curr_max = max(curr_max, max_envlp_count[j])
            
            max_envlp_count[i]=curr_max+1
            max_count = max(max_count, max_envlp_count[i])

        return max_count