"""
Problem Description
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.
"""

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, s):
        # check if the string is a palindrome
        if s==s[::-1]:
            return 0
        n = len(s)
        # check for 1 cut
        for i in range(1, n):
            if s[:i]==s[:i][::-1] and s[i:]==s[i:][::-1]:
                return 1 
        
        # matrix to store is_palindrome True/False i.e 0/1
        is_palindrome_matrix = [[False]*(i+1) for i in range(n)]
        min_cut_list = [0]*(n+1)
        for i in range(n+1):
            min_cut_list[i]=i
        # set the last value as -1 to compensate for +1 we do for each cut 
        min_cut_list[n]=-1

        for r in range(n):
            for c in range(r, -1, -1):
                if s[r]==s[c] and ( r-c < 2 or is_palindrome_matrix[r-1][c+1]):
                    is_palindrome_matrix[r][c]=True
                    min_cut_list[r] = min(min_cut_list[r], min_cut_list[c-1] + 1)
        
        return min_cut_list[n-1]