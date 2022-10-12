"""
Problem Description
Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B

Note:

There are no self-loops in the graph.

No multiple edges between two pair of vertices.

The graph may or may not be connected.

Nodes are Numbered from 0 to A-1.

Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # build the adjacency list
        adjacency_list = {}
        for x in B:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append(x[1])
            else:
                adjacency_list[x[0]] = [x[1]]
            
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append(x[0])
            else:
                adjacency_list[x[1]] = [x[0]]

        from collections import deque
        # Q to store the vertices
        dq = deque([])

        # -1 means NO color 
        # 1 means Red, 2 means Blue
        vertex_color = [-1]*(A)
        for i in range(A):
            # if not colored 
            if vertex_color[i]==-1:
                # color it Red
                dq.append((i,1))
                # update the vertex color list
                vertex_color[i]=1
                while dq:
                    curr = dq.popleft()
                    curr_vertex = curr[0]
                    curr_color = curr[1]

                    if curr_vertex not in adjacency_list:
                        #print(curr_vertex, "not found")
                        continue

                    for j in adjacency_list[curr_vertex]:
                        if vertex_color[j]==curr_color:
                            return 0 
                        
                        # NOT colored
                        if vertex_color[j]==-1:
                            if curr_color==1:           # Vertex Red
                                vertex_color[j]=2       # Neighbour Blue 
                            elif curr_color==2:         # Vertex Blue 
                                vertex_color[j]=1       # Neighbour Red 
                            # add to Q
                            dq.append((j, vertex_color[j]))
                
        return 1