import csv 
class Graph: 
    def __init__(self):
        self._graph = {}

    def best_path_search(start_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the shortest path from a source vertex to a destination vertex.'''
        pass

    def add_vertex(self, vertex):
        '''Adds a vertex to the graph. Takes the vertex name and a variable number of adjacency tuples as arguement. Each tuple consists of an 
        adjacent vertex and cost.'''
        pass
        # self._graph[vertex] = {}

    def delete_vertex(self, vertex):
        '''Deletes a vertex with the given name and all its incident edges.'''
        pass

    def add_edge(self, vertex1, vertex2, cost):
        pass 


    def vertex_exists(self, vertex):
        '''Returns true if a vertex with a given name exists on the graph.'''
        pass 


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


if __name__ == '__main__':
    main()