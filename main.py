import csv 
class Graph: 
    def __init__(self):
        self._graph = {}

    def best_path_search(start_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the shortest path from a source vertex to a destination vertex.'''
        pass

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

def main():
    map = Graph()
    
    with open('adjacencies.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader: 
            if not map.vertex_exists(row[0]):
                map.add_vertex(row[0])

            if not map.vertex_exists(row[1]):
                map.add_vertex(row[1])

            map.add_edge(row[0], row[1], row[2])
            
    print(map.get_graph())

if __name__ == '__main__':
    main()