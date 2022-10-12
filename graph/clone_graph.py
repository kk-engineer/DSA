"""
Problem Description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
First integer N is the number of nodes.
Then, N intgers follow denoting the label (or hash) of the N nodes.
Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.

"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        from collections import deque
        dq = deque([])
        dq.append(node)
        head_created = False
        clone_head = None
        while dq:
            curr_node = dq.popleft()
            temp = UndirectedGraphNode(curr_node.label)
            temp.neighbors = list(curr_node.neighbors)
            self.visited[curr_node] = temp  
            if not head_created:
                clone_head = temp 
                head_created = True
                
            for nbr in curr_node.neighbors:
                if nbr not in visited:
                    dq.append(nbr)
        
        return clone_head
