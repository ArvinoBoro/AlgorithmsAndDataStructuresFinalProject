import heapq
import math

class Graph: 
    def __init__(self):
        self._graph = {} 

    def best_path_search(self, source_vertex, end_vertex): 
        '''Uses Dijkstra's Algorithm to find the lowest path weight from a source vertex to a destination vertex. Takes the source vertex name and destination vertex name as arguement.
        Returns the path as a list, and the cumulative path weight.'''
        # Note: neighbour is the term used for adjacent vertex.
        if not (self.vertex_exists(source_vertex) and self.vertex_exists(end_vertex)):
            print("Error: The source and end vertices do not exist.")
            return None
        
        if not self.vertex_exists(source_vertex):
            print("Error: The source vertex does not exist.")
            return None

        if not self.vertex_exists(end_vertex):
            print("Error: The end vertex does not exist.")
            return None

        visited_vertices = set() 
        lowest_path_weights = {vertex: [math.inf, None] for vertex in self._graph} 
        lowest_path_weights[source_vertex] = [0, None]

        priority_queue = []
        heapq.heapify(priority_queue)   # Initializes a minheap priority queue.
        heapq.heappush(priority_queue, (0, source_vertex))  # Pushes the source vertex and its path weight of 0 to the priority queue.

        while priority_queue:
            current_weight, current_vertex = heapq.heappop(priority_queue) 

            if not current_vertex in visited_vertices:  # Checks if the vertex at the front of the queue was already visisted.
                visited_vertices.add(current_vertex)    # Adds the newly visisted vertex to the set of visited vertices.

                for neighbour, neighbour_weight in self._graph[current_vertex].items():   # Iterates through each neighbouring vertex of the current vertex and the path weight to the neighbour.
                    if neighbour not in visited_vertices:   # Checks if the neighbour was already visisted.
                        new_weight = current_weight + neighbour_weight    # Updates the path weight to the neighbour. 
                        if new_weight < lowest_path_weights[neighbour][0]:   # Checks if the path to the neighbouring vertex has a lower weight than the weight already in lowest_path_weights.
                            lowest_path_weights[neighbour][0] = new_weight   # Assigns the lower path weight to the lowest_path_weights entry for the neighbour.
                            lowest_path_weights[neighbour][1] = current_vertex     # Assigns the previous vertex of the neighbour's lowest weighing path to the currently visisted vertex.
                            heapq.heappush(priority_queue, (new_weight, neighbour))   # Pushes the neighbour with its new cost to the priority queue, heapifying as well.

        path = []
        current_vertex = end_vertex
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = lowest_path_weights[current_vertex][1]
        path.reverse()  # Extracts the path from the source vertex to end destination vertex.

        total_path_weight = lowest_path_weights[end_vertex][0]
        return (path, total_path_weight)   # Returns the path from the source vertex to destination vertex and the total path weight. 

    def add_vertex(self, vertex):
        '''Adds a vertex to the graph without forming any adjacencies. Takes the vertex name as arguement.'''
        if self.vertex_exists(vertex):
            print("Error: The vertex already exists.")
            return None
        self._graph[vertex] = {}

    def delete_vertex(self, vertex):
        '''Deletes a vertex and all its incident edges. Takes the vertex name as arguement.'''
        if self.vertex_exists(vertex):
            print("Error: The vertex does not exist.")
            return None
        for affected_vertex in self._graph[vertex].keys():
            print(affected_vertex)
            self._graph[affected_vertex].pop(vertex)
        del self._graph[vertex]

    def add_edge(self, vertex1, vertex2, weight=0):
        '''Creates an undirected edge between two vertices. Takes the names of the vertices and the weight.'''
        if not (self.vertex_exists(vertex1) and self.vertex_exists(vertex2)):
            print("Error: The vertices do not exist.")
            return None
        
        if not self.vertex_exists(vertex1):
            print("Error: The first vertex does not exist.")
            return None

        if not self.vertex_exists(vertex2):
            print("Error: The second vertex does not exist.")
            return None
        self._graph[vertex1][vertex2] = weight
        self._graph[vertex2][vertex1] = weight


    def vertex_exists(self, vertex):
        '''Returns true if a vertex with a given name exists on the graph.'''
        return vertex in self._graph
    
    def get_graph(self):
        '''Returns the dictionary attribute storing the graph.'''
        return self._graph 
    
    def vertex_count(self):
        '''Returns the number of vertices in the graph as the number of entries in the dictionary attribute.'''
        return len(self._graph)