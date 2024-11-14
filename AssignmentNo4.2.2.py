# Function to print the color assignments of vertices
def print_coloring(color, V):
    for i in range(V):
        print(f"Vertex {i + 1} --> Color {color[i]}")

# Check if it's safe to color vertex `ver` with color `c`
def is_safe(graph, V, c, color, ver):
    for i in range(V):
        if graph[ver][i] == 1 and color[i] == c:  # Adjacent vertex has the same color
            return False
    return True

# Backtracking function to color the graph
def color_graph(graph, m, color, V, ver):
    if ver == V:  # All vertices have been assigned a color
        return True
    
    # Try all colors for vertex `ver`
    for c in range(1, m + 1):
        if is_safe(graph, V, c, color, ver):  # Check if it's safe to color vertex `ver` with color `c`
            color[ver] = c  # Assign color to vertex
            
            # Recur to color the next vertex
            if color_graph(graph, m, color, V, ver + 1):
                return True
            
            color[ver] = -1  # Backtrack if no valid coloring is found
    
    return False  # No valid coloring is possible for vertex `ver`

def main():
    # Read input for number of vertices and edges
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    
    # Initialize the graph (adjacency matrix)
    graph = [[0 for _ in range(V)] for _ in range(V)]
    
    print("\nStart entering edges (u, v) where u and v are 1-based indices:")
    for _ in range(E):
        u, v = map(int, input("Edge [u, v]: ").split())
        graph[u - 1][v - 1] = 1  # Adjusting for zero-based indexing
        graph[v - 1][u - 1] = 1  # As the graph is undirected
    
    # Read the number of colors
    m = int(input("Enter the minimum number of colors: "))
    
    # Initialize all vertices as uncolored (-1)
    color = [-1] * V
    
    # Try to color the graph using backtracking
    if color_graph(graph, m, color, V, 0):
        print_coloring(color, V)
    else:
        print(f"Coloring not possible with {m} colors.")

# Run the main function
if __name__ == "__main__":
    main()
