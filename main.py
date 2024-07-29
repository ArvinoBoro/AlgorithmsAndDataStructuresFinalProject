import csv 
import heapq
import math
class Graph: 
    def __init__(self):
        self._graph = {}

    def best_path_search(self, source_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the shortest path from a source vertex to a destination vertex.'''
        visited_vertices = set() 
        lowest_costs = {vertex: [math.inf, None] for vertex in self._graph} 
        lowest_costs[source_vertex] = [0, None]

        priority_queue = []
        heapq.heapify(priority_queue)   # Initializes a minheap priority queue.
        heapq.heappush(priority_queue, (0, source_vertex))  # Pushes the source vertex and its path cost to the priority queue.

        while priority_queue:
            current_cost, current_vertex = heapq.heappop(priority_queue) 

            if not current_vertex in visited_vertices:  # Checks if the vertex at the front of the queue was already visisted.
                visited_vertices.add(current_vertex) 

                for neighbour, weight in self._graph[current_vertex].items():   # Iterates through each neighbouring vertex from the current vertex and the path weight to the neighbour.
                    if neighbour not in visited_vertices:
                        new_cost = current_cost + weight        
                        if new_cost < lowest_costs[neighbour][0]:   # Checks if the path to the neighbouring vertex has a lower cost than the current cost in shortest_paths
                            lowest_costs[neighbour][0] = new_cost   # Assigns the lowest cost to the neighbour to the new cost.
                            lowest_costs[neighbour][1] = current_vertex     # Assigns the previous vertex of the neighbour's lowest cost path to the currently visisted vertex.
                            heapq.heappush(priority_queue, (new_cost, neighbour))   # Pushes the neighbour with its new cost to the priority queue, heapifying as well.

        print(lowest_costs, end='\n\n')

    def add_vertex(self, vertex):
        '''Adds a vertex to the graph without forming any adjacencies. Takes the vertex name as arguement.'''
        self._graph[vertex] = {}

    def delete_vertex(self, vertex):
        '''Deletes a vertex and all its incident edges. Takes the vertex name as arguement.'''
        for affected_vertex in self._graph[vertex].keys():
            print(affected_vertex)
            self._graph[affected_vertex].pop(vertex)
        
        del self._graph[vertex]

    def add_edge(self, vertex1, vertex2, weight=0):
        '''Creates an undirected edge between two vertices. Takes the names of the vertices and the weight.'''
        self._graph[vertex1][vertex2] = weight
        self._graph[vertex2][vertex1] = weight


    def vertex_exists(self, vertex):
        '''Returns true if a vertex with a given name exists on the graph.'''
        return vertex in self._graph
    
    def get_graph(self):
        return self._graph 
    
    def vertex_count(self):
        return len(self._graph)

def main():
    map = Graph()
    
    with open('adjacencies.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader: 
            if not map.vertex_exists(row[0]):
                map.add_vertex(row[0])

            if not map.vertex_exists(row[1]):
                map.add_vertex(row[1])

            map.add_edge(row[0], row[1], int(row[2]))
    
    map.best_path_search('S', 'D')
    #print(map.get_graph())

if __name__ == '__main__':
    main()