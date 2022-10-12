"""
Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

Input Format:

The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
Constraints:

1 <= len(A) <= 6500
1 <= len(B) <= 10000
1 <= len(B[i]) <= 20
Examples:

Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]

Output 1:
    1

Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

Input 2:
    A = "a"
    B = ["aaa"]

Output 2:
    0

Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".
"""

class Solution:

	# @param A : string
	# @param B : list of strings
	# @return an integer

	def wordBreak(self, A, B):
        # add all the dictionary words to a set for faster lookup
		sample_set = set()
		for x in B:
			sample_set.add(x)

		n = len(A)
        # initialise the DP that stores whether its possible to segment the input 
        # starting from ith index till end into a space-separated sequence of one or more
        # dictionary words - with False
		word_break = [False]*(n+1)
        # initialise the end index + 1 position  as True 
		word_break[n] = True 

		for i in range(n-1, -1, -1):
			for j in range(i, n):
                # check whether the string formed from current till last index is present in the set
                # and then check the status of word_break starting next index 
				if A[i:j+1] in sample_set and word_break[j+1]:
					word_break[i] = True
                    break
                    
		return 1 if word_break[0] else 0
