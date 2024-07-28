import csv 
import queue
import math
class Graph: 
    def __init__(self):
        self._graph = {}

    def best_path_search(self, source_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the shortest path from a source vertex to a destination vertex.'''
        visisted_vertices = []
        shortest_paths = {} # The key is the destination vertex. The value is the cost.
    
        for vertex in self._graph:      # Iterates through each and every vertex in the graph.
            if vertex == source_vertex:     
                shortest_paths[vertex] = [0, None]          # The cost to the source vertex is always 0.
            else:
                shortest_paths[vertex] = [math.inf, None]   # The cost to any other destination vertex starts off as infinity.
        print(shortest_paths, end='\n\n')

        def visit(vertex):
            visisted_vertices.append(vertex)                
            lowest_cost_path = math.inf

            for neighbour in self._graph[vertex].keys():                # Iterates through each vertex that is adjacent to the currently visisted vertex.
                if not neighbour in visisted_vertices:                  # Checks if the neighbouring vertex was already visisted.
                    if self._graph[vertex][neighbour] + shortest_paths[vertex][0] < shortest_paths[neighbour][0]:       # Checks if the path to the neighbouring vertex has a lower cost than the current cost in lowest_cost_path.
                        shortest_paths[neighbour][0] = self._graph[vertex][neighbour] + shortest_paths[vertex][0]       # Sets the current lowest cost path to the neighbouring vertex as the sum of the total path cost to the currently visisted vertex and the path cost between the currently visisted vertex and neighbouring vertex.
                        shortest_paths[neighbour][1] = vertex       # Makes the previous vertex for the shortest path to the neighbouring vertex the currently visisted vertex.
                    if shortest_paths[neighbour][0] < lowest_cost_path:     # Checks if the cost from the currently visisted vertex to the neighbour is the lowest among all iterated neighbours.
                        lowest_cost_path = shortest_paths[neighbour][0]
                        next_neighbour = neighbour      # The next vertex to be visisted has the lowest cost from the currently visisted vertex.

            
            print(shortest_paths, end='\n\n')
            
            if len(visisted_vertices) < len(self._graph):       # Checks if all vertices in the graph have been visisted.   
                visit(next_neighbour)       # Recursively visits the next neighbour.
  
        visit(source_vertex)


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
    
    map.best_path_search('A', 'A')

if __name__ == '__main__':
    main()