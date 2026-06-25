# City Traffic Navigation System Using Graph Data Structure
# Uses Dijkstra's Algorithm to find the shortest path

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, distance):
        if source not in self.graph:
            self.graph[source] = []

        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))  # Undirected graph

    def dijkstra(self, start, end):
        priority_queue = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end

        while current:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, distances[end]


def main():
    city = Graph()

    # Sample City Road Network
    city.add_edge("A", "B", 4)
    city.add_edge("A", "C", 2)
    city.add_edge("B", "D", 5)
    city.add_edge("C", "D", 8)
    city.add_edge("C", "E", 10)
    city.add_edge("D", "E", 2)
    city.add_edge("D", "F", 6)
    city.add_edge("E", "F", 3)

    print("======================================")
    print(" CITY TRAFFIC NAVIGATION SYSTEM ")
    print(" USING GRAPH DATA STRUCTURE")
    print("======================================")

    print("\nAvailable Locations:")
    for location in city.graph.keys():
        print(location, end=" ")
    print()

    source = input("\nEnter Source Location: ").upper()
    destination = input("Enter Destination Location: ").upper()

    if source not in city.graph or destination not in city.graph:
        print("Invalid Location!")
        return

    path, distance = city.dijkstra(source, destination)

    print("\n===== SHORTEST ROUTE =====")
    print("Route:", " -> ".join(path))
    print("Total Distance:", distance, "Units")
    print("==========================")

if __name__ == "__main__":
    main()