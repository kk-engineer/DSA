"""
Given a string A and a dictionary of words B, add spaces in A to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Note : Make sure the strings are sorted in your result.
"""

class Solution:
    """
    Reference: https://leetcode.com/problems/word-break-ii/discuss/1675304/Short-Python-bottom-up-DP
    """

	# @param A : string
	# @param B : list of strings
	# @return a list of strings

    def wordBreak(self, A, B):
        # add all the words in a dictionary to a set for faster look-up
        word_set = set()
        for x in B:
            if x not in word_set:
                word_set.add(x)

        n = len(A)
        # starting from last index check whether its possible to break that word in a valid word 
        # present in dictionary
        word_possible = [False]*(n+1)
        # set the last index as True
        word_possible[n]=True

        ans = [[""]]

        for i in range(n-1, -1, -1):
            temp = []
            for j in range(i, n):
                if A[i:j+1] in word_set and word_possible[j+1]:
                    word_possible[i]=True
                    #print("Begin", i, j, n-1-j, ans[n-1-j], A[i:j+1])
                    for item in ans[n-1-j]:     # (n-1 - j: ranges from n-1 to 0)
                        # if empty string, add tje current word to temp 
                        if item=="":
                            temp.append(A[i:j+1])
                        # else add the word + " " before the existing item and add it to ans string list
                        else:
                            temp.append(A[i:j+1] + " " + item)
                
            ans.append(temp) 
            #print("End", i, ans)  
        
        return ans[-1]