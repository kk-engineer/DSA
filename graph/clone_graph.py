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