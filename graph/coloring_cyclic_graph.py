"""
Problem Description
Given the number of vertices A in a Cyclic Graph.

Your task is to determine the minimum number of colors required to color the graph so that no two Adjacent vertices have the same color.
"""

class Solution:
    """
    Ref: https://www.geeksforgeeks.org/coloring-a-cycle-graph/
    """
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return 3 if A%2 else 2