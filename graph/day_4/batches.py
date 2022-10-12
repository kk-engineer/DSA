"""
Problem Description

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.
"""

class Solution:
    def get_adjacency_list(self, adjacency_matrix):
        adjacency_list = {}
        for x in adjacency_matrix:
            if x[0] in adjacency_list:
                adjacency_list[x[0]].append(x[1])
            else:
                adjacency_list[x[0]] = [x[1]]
            
            # the reverse edge, since un-directed 
            if x[1] in adjacency_list:
                adjacency_list[x[1]].append(x[0])
            else:
                adjacency_list[x[1]] = [x[0]]
            
        return adjacency_list

    def dfs(self, vertex, visited, adjacency_list, curr_strength, B, D):
        # add the vertex to visited
        visited.add(vertex)
        # add the current vertex strength 
        curr_strength[0]+=B[vertex-1]
        
        if vertex in adjacency_list:
            for neighbour in adjacency_list[vertex]:
                if neighbour not in visited:
                    self.dfs(neighbour, visited, adjacency_list, curr_strength, B, D)

    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        # default recursion stack is 1000 
        #print(sys.getrecursionlimit())
        sys.setrecursionlimit(10**5)
        # build an adjacency list first
        adjacency_list = self.get_adjacency_list(C)

        #print(adjacency_list)
        # set to store visited vertices
        visited = set()
        batch_count = 0
        for v in range(1, A+1):
            if v not in visited:
                curr_strength = [0]
                # Instead of integerpass integer as list or a class object   
                # because integers are immutable in python 
                # and everytime we do "=" a new variable is created
                self.dfs(v, visited, adjacency_list, curr_strength, B, D)

                # check if the current strength is greater than required batch strength D
                # if yes , increment the batch count by 1
                if curr_strength[0]>=D:
                    batch_count+=1
        
        return batch_count