"""
Problem Description

Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.

Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

NOTE:

Level and Depth of the root is considered as 0.
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Please read the input format for more clarification.

Input Format

The first argument is an integer A denoting the number of nodes.

The second and third arguments are the integer arrays B and C where for each i (0 <= i < A-1), B[i] and C[i] are the nodes connected by an edge.

The fourth argument is an integer array D, where D[i] denotes the value of the (i+1)th node

The fifth and sixth arguments are the integer arrays E and F where for each i (0 <= i < Q), E[i] denotes L and F[i] denotes X for ith query.

Output Format

Return an array of integers where the ith element denotes the answer to ith query.
"""

class Solution:
    def BFS(self, adj_list, D):
        level_list = {}
        from collections import deque
        dq = deque([])
        # add 1 to the dq; add a tuple of (1, 0), 0 is its level 
        dq.append((1,0))
        visited = set()
        max_depth = 0
        while (dq):
            curr = dq.popleft()
            curr_vertex, curr_level = curr[0], curr[1]
            # update the max_depth 
            max_depth = max(max_depth, curr_level)
            # mark the current vertex as visited 
            visited.add(curr_vertex)
            if curr_level in level_list:
                level_list[curr_level].append(D[curr_vertex - 1])
            else:
                level_list[curr_level] = [D[curr_vertex - 1]]
            
            if curr_vertex in adj_list:
                for nbr in adj_list[curr_vertex]:
                    if nbr not in visited:
                        dq.append((nbr, curr_level+1))
        
        return level_list, max_depth

    def get_adj_list(self, B, C):
        adj_list = {}
        n = len(B)
        for i in range(n):
            if B[i] in adj_list:
                adj_list[B[i]].append(C[i])
            else:
                adj_list[B[i]] = [C[i]]
            
            if C[i] in adj_list:
                adj_list[C[i]].append(B[i])
            else:
                adj_list[C[i]] = [B[i]]
        
        return adj_list

    def binary_search(self, A, target):
        n = len(A)
        L, R = 0, n-1
        ans = -1
        while L<=R:
            mid = (L+R)//2
            if A[mid]==target:
                return A[mid]
            elif A[mid]>target:
                ans = A[mid]
                R = mid-1
            else:   # A[mid] < target
                L = mid+1
        
        return ans

    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):
        # get the adjacency list
        adj_list = self.get_adj_list(B, C)
        # do a BFS get the map of depth: [list of vertex[values]], and max_depth
        level_list, max_depth = self.BFS(adj_list, D)
        # sort the values for each level 
        for key, value in level_list.items():
           level_list[key] = sorted(value)
        
        n = len(E)
        ans = []
        for i in range(n):
            # check if the current query depth is greater than the max_depth+1
            E[i]%=(max_depth+1)
            # binary search for target F[i] in sorted level_list[E[i]]
            curr_ans = self.binary_search(level_list[E[i]], F[i])
            ans.append(curr_ans)
        
        return ans