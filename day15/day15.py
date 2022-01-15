#!/usr/bin/python3

### DAY 15.1

'''
Start at the top left position, destination is the bottom right position.
Moving diagonally is not allowed.
Find out which is the path that has the lowest risk level, which is calculated adding up all the risk levels of the positions you enter WITHOUT taking into account the starting position unless you enter it at some point.
'''

import numpy as np
from math import inf
from heapq import heappop, heappush
from datetime import datetime

def parse_data():
    with open('input.txt','r') as f:
        edges = [[i for i in map(int, list(line.strip()))] for line in f.readlines()]
    return edges

def get_neighbours(i,j, graph):
    rightBound = len(graph[0])
    botomBound = len(graph)
    adjacentNodes = []
    for y, x in [(-1,0),(1,0),(0,-1),(0,1)]:
        neighbour_y = i + y
        neighbour_x = j + x
        if 0 <= neighbour_y < botomBound and 0 <= neighbour_x < rightBound:
            adjacentNodes.append((neighbour_y, neighbour_x)) #remember that first coord is telling the vertical position and second coord the horizontal position in the original matrix
    return adjacentNodes

def relaxation(neighbours, edges, distances, unvisited_set, node_queue):
    for neighbour in neighbours:
        if neighbour in unvisited_set:
            d = edges[neighbour[0]][neighbour[1]]
            tentative_distance = distances[neighbour[0]][neighbour[1]]
            if c_node_d + d < tentative_distance:
                distances[neighbour[0]][neighbour[1]] = c_node_d + d
            heappush(node_queue, (distances[neighbour[0]][neighbour[1]], neighbour))
        else:
            continue
    return distances, node_queue


startTime = datetime.now()

edges = np.array(parse_data())
edges[0][0] = 0
distances = np.full((len(edges), len(edges[0])), fill_value=inf)
distances[0][0] = 0
node_queue = []
heappush(node_queue, (0, (0,0)))
destination_node = (len(edges)-1, len(edges[-1])-1)
unvisited_set = set((y, x) for x in range(len(edges[0])) for y in range(len(edges)))

while destination_node in unvisited_set:
    c_node_d, c_node_coords = heappop(node_queue) #extract the smallest value in the heap
    if c_node_coords not in unvisited_set:
        continue
    neighbours = get_neighbours(c_node_coords[0], c_node_coords[1], edges)
    distances, node_queue = relaxation(neighbours, edges, distances, unvisited_set, node_queue)
    unvisited_set.remove(c_node_coords)

print(distances[-1][-1])
print(datetime.now() - startTime)


