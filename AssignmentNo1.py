def a_star(start, goal, graph, heuristics):
    open_set = {start}
    g_values = {start: 0}  # Cost to reach the start
    parents = {start: None}

    while open_set:
        # Select the node with the lowest f = g + h
        current = min(open_set, key=lambda node: g_values[node] + heuristics[node])
        
        if current == goal:  # If we reached the goal, reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path

        open_set.remove(current)
        
        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            g_cost = g_values[current] + weight
            if neighbor not in g_values or g_cost < g_values[neighbor]:
                g_values[neighbor] = g_cost
                parents[neighbor] = current
                open_set.add(neighbor)

    return None  # No path found

def get_input():
    # Input graph and heuristic values from the user
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    num_edges = int(input("Enter number of edges: "))
    graph = {}
    for _ in range(num_edges):
        u, v, w = input("Enter edge (node1 node2 weight): ").split()
        w = int(w)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))  # Assuming undirected graph
    
    heuristics = {}
    for node in graph:
        heuristics[node] = int(input(f"Enter heuristic value for {node}: "))

    return start, goal, graph, heuristics

if __name__ == "__main__":
    start, goal, graph, heuristics = get_input()
    path = a_star(start, goal, graph, heuristics)

    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found.")


 
# Enter start node: S
# Enter goal node: D
# Enter number of edges: 7
# Enter edge (node1 node2 weight): S A 1
# Enter edge (node1 node2 weight): S B 4
# Enter edge (node1 node2 weight): A B 2
# Enter edge (node1 node2 weight): A C 5
# Enter edge (node1 node2 weight): A D 12 
# Enter edge (node1 node2 weight): B C 2
# Enter edge (node1 node2 weight): D C 3
# Enter heuristic value for S: 7
# Enter heuristic value for A: 6
# Enter heuristic value for B: 2
# Enter heuristic value for C: 1
# Enter heuristic value for D: 0
# Path found: S -> A -> B -> C -> D 