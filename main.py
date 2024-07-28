import csv 
import queue
import math
class Graph: 
    def __init__(self):
        self._graph = {}

    def best_path_search(self, source_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the shortest path from a source vertex to a destination vertex.'''
        visisted_vertices = []
        shortest_paths = {}
    
        for vertex in self._graph:
            if vertex == source_vertex:
                shortest_paths[vertex] = [0, None]
            else:
                shortest_paths[vertex] = [math.inf, None]
        print(shortest_paths, end='\n\n')

        def visit(vertex):
            visisted_vertices.append(vertex)
            lowest_cost_path = math.inf

            for neighbour in self._graph[vertex].keys():
                if not neighbour in visisted_vertices:
                    if self._graph[vertex][neighbour] + shortest_paths[vertex][0] < shortest_paths[neighbour][0]:
                        shortest_paths[neighbour][0] = self._graph[vertex][neighbour] + shortest_paths[vertex][0]
                        shortest_paths[neighbour][1] = vertex
                    if shortest_paths[neighbour][0] < lowest_cost_path:
                        lowest_cost_path = shortest_paths[neighbour][0]
                        next_neighbour = neighbour 

            print(shortest_paths, end='\n\n')
            
            
            if len(visisted_vertices) < len(self._graph):
                visit(next_neighbour)
  
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