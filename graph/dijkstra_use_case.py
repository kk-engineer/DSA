"""
Problem Description
Sheldon lives in a country with A cities (numbered from 1 to A) and B bidirectional roads.

Roads are denoted by integer array D, E and F of size M, where D[i] and E[i] denotes the cities and F[i] denotes the distance between the cities.

Now he has many lectures to give in the city and is running short of time, so he asked you C queries, for each query i, find the shortest distance between city G[i] and H[i].

If the two cities are not connected then the distance between them is assumed to be -1.
"""

import heapq 
# Dijkstra use case 
class Solution:
    def get_adj_list(self, B, D, E, F):
        adj_list = {}
        for i in range(B):
            if D[i] in adj_list:
                adj_list[D[i]].append((E[i], F[i]))
            else:
                adj_list[D[i]] = [(E[i], F[i])]
            
            # add the reverse edges too 

            if E[i] in adj_list:
                adj_list[E[i]].append((D[i], F[i]))
            else:
                adj_list[E[i]] = [(D[i], F[i])]
        
        return adj_list

	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : list of integers
	# @param E : list of integers
	# @param F : list of integers
	# @param G : list of integers
	# @param H : list of integers
	# @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):
        # build the adjacency list first 
        adj_list = self.get_adj_list(B, D, E, F)
        ans = []
       
        distance_map = {}
        for i in range(C):
            if G[i] in distance_map:
                curr_distance_list = distance_map[G[i]] 
                ans.append(curr_distance_list[H[i]])
                continue

            distance = [sys.maxsize]*(A+1) 
            # initialise the source distance with 0 
            distance[G[i]]=0
            min_heap = []
            # insert a tuple with distance first in the min heap, 
            # so that the distance will be used to build the min_heap
            heapq.heappush(min_heap, (0, G[i]) )

            # keep going until the min heap is not empty 
            while min_heap:
                #pop the curr minimum distance vertex 
                curr = heapq.heappop(min_heap)
                curr_distance, curr_vertex = curr[0], curr[1]

                # check if the current vertex is present in the adjacency list 
                if curr_vertex in adj_list:
                    # check for all the neighbours
                    for nbr in adj_list[curr_vertex]:
                        nbr_vertex = nbr[0]
                        nbr_wt = nbr[1]
                        # add current vertex distance to the neighbour's weight 
                        # to get the actual neighbour distance 
                        nbr_distance = curr_distance + nbr_wt 
                        
                        # compare the current neighbour distance with the distance stored in distance map 
                        # if less update the distance and push the new neighbour to min heao 
                        if nbr_distance<distance[nbr_vertex]:
                            distance[nbr_vertex] = nbr_distance 
                            heapq.heappush(min_heap, (nbr_distance, nbr_vertex))
                
            for j in range(A+1):
                if distance[j]==sys.maxsize:
                    distance[j]=-1
            
            if G[i] not in distance_map:
                distance_map[G[i]] = distance
        
            # append the ans with the distance of the destination node
            ans.append(distance[H[i]])
        
        return ans 
