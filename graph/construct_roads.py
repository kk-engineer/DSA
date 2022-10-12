"""
Problem Description
A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.
"""

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        # build the adjacency list first 
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

        # set to store all visited vertices
        visited = set()
        red_set, blue_set = set(), set()
        for v in range(1, A+1):
            if v not in visited:
                # add to visited 
                visited.add(v)

                from collections import deque
                dq = deque([])
                # add it to red set by default
                dq.append((v,'R'))
                red_set.add(v)

                #BFS
                while dq:
                    curr = dq.popleft()
                    # check if we have roads from current vertex 
                    if curr[0] in adjacency_list:
                        # check all its neighbours 
                        for neighbour in adjacency_list[curr[0]]:
                            # do only for neighbours not visited yet 
                            if neighbour not in visited:
                                # if current vertex Red, mark neighbours Blue
                                if curr[1]=='R':
                                    dq.append((neighbour, 'B'))
                                    blue_set.add(neighbour)
                                # if current vertex Blue, mark neighbours Red
                                elif curr[1]=='B':
                                    dq.append((neighbour, 'R'))
                                    red_set.add(neighbour)

                                # add the neighbour to visited 
                                visited.add(neighbour)

        # total number of roads possible = n1 * n2 
        total_roads = len(red_set) * len(blue_set)
        # A-1 roads already present,
        # so max roads that can be constructed = difference of above 2 
        max_roads = total_roads - (A-1)

        return max_roads%(10**9 + 7 )