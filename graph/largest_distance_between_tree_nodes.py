"""
Problem Description
Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes.

The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.
"""

class Solution:
    """
    Reference: https://www.geeksforgeeks.org/longest-path-undirected-tree/
    We can find the maximum distance by 2 BFS - 
    1. finding first the farthest node from the root, say N1
    2. Then find the farthest node , say N2,  from the node N1 found in previous step
    """
    def get_adj_list(self, A):
        adj_list = {}
        n = len(A)
        for i in range(n):
            if A[i]==-1:
                continue

            if A[i] in adj_list:
                adj_list[A[i]].append(i)
            else:
                adj_list[A[i]] = [i]
            
            # reverse edges 
            if i in adj_list:
                adj_list[i].append(A[i])
            else:
                adj_list[i] = [A[i]]
        
        return adj_list

    def BFS (self, vertex, adj_list):
        from collections import deque
        dq = deque([])
        dq.append((vertex, 0))
        max_distance, target_vertex = 0, vertex
        visited = set()
        while dq:
            curr = dq.popleft()
            curr_vertex, curr_distance = curr[0], curr[1]
            # mark as visited
            visited.add(curr_vertex)

            if curr_vertex in adj_list:
                for nbr in adj_list[curr_vertex]:
                    if nbr not in visited:
                        nbr_distance = curr_distance + 1
                        # add the nbr to Q 
                        dq.append((nbr, nbr_distance))
        
                        # check if distance is greater than max distance till now, update
                        if nbr_distance>max_distance:
                            max_distance = nbr_distance
                            target_vertex = nbr
        
        return max_distance, target_vertex

	# @param A : list of integers
	# @return an integer
    
    def solve(self, A):
        # get the adjacency list 
        adj_list = self.get_adj_list(A)
        
        root = -1
        for i, v in enumerate(A):
            if v==-1:
                root = i 
                break
        
        # get the farthest node from the root
        distance, target_vertex = self.BFS(root, adj_list)

        # use the target node as source for BFS and get the farthest node from it 
        max_distance, vertex = self.BFS(target_vertex, adj_list)

        return max_distance