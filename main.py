from graph import Graph
import csv 

def get_input():
    while True:
        user_input = input("Enter a starting point (every letter except 'x', 'y', 'z'): ").upper()

        if len(user_input) == 1 and user_input.isalpha() and user_input not in ['X', 'Y', 'Z']:
            return user_input
        else:
            print("Error: Input must be a single letter, excluding 'x', 'y', and 'z'.")

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

    starting_point = get_input()
    end_points = ['H', 'K', 'Q', 'T']

    for end_point in end_points:
        path, shortest_path_cost = map.best_path_search(starting_point, end_point)
        print(f"\nEnd Point: {end_point}")
        print(f"Shortest Path Cost: {shortest_path_cost}")
        print(f"Path: {' -> ' .join(path)}")

if __name__ == '__main__':
    main()