class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list representation

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        result = [None] * self.V
        colors = ["Red", "Green", "Blue"]  # Color list
        
        # Assign the first color
        result[0] = "Red"

        # Assign colors to remaining vertices
        for u in range(1, self.V):
            # Set of available colors (start with all colors)
            available_colors = set(colors)

            # Mark colors of adjacent vertices as unavailable
            for v in self.graph[u]:
                if result[v] is not None:
                    available_colors.discard(result[v])

            # Assign the first available color (if any)
            if available_colors:
                result[u] = available_colors.pop()
 
        print("\nColoring of vertices:")
        for u in range(self.V):
            print(f"Vertex {u} --> Color {result[u]}")
 
if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    graph = Graph(vertices)

    edges = int(input(f"Enter the number of edges in the graph: "))

    print("Enter the edges (u v) where u and v are vertex indices:")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
 
    graph.greedy_coloring()

 