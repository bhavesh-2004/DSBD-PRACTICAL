 # Initial values for Alpha and Beta
MAX, MIN = 10000000, -10000000

def minimax(depth, index, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[index]
    
    #maximizing Player
    if maximizingPlayer:
        optimum = MIN
        # Explore the left and right children
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, False, values, alpha, beta)
            optimum = max(optimum, val)
            alpha = max(alpha, optimum)
            # Alpha-Beta Pruning 
            if beta <= alpha:
                break
        return optimum
    else:
        # Minimizing player  
        optimum = MAX
        # Explore the left and right children
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, True, values, alpha, beta)
            optimum = min(optimum, val)
            beta = min(beta, optimum)
            # Alpha-Beta Pruning:
            if beta <= alpha:
                break
        return optimum

if __name__ == "__main__":
    #inputs
    num_values = int(input("Enter the number of leaf nodes: "))
    print(f"Enter {num_values} values for the leaf nodes:")

    values = []
    for i in range(num_values):
        value = int(input(f"Enter value {i+1}: "))
        values.append(value)
    
    # Print the optimal value starting from the root node
    print("The optimum value is:", minimax(0, 0, True, values, MIN, MAX))
