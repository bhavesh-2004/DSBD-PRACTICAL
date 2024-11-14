
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col:  # Check if any queen is already in the same column
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:   
            return False

    # Check the upper diagonal on the right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i] == j:   
            return False

    return True

def solve_nqueens_util(board, row, N, solutions):
    # Base case
    if row >= N:
        solutions.append(board[:]) 
        return

    for col in range(N):
        if is_safe(board, row, col, N): 
            board[row] = col  # Place the queen at (row, col)
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row] = -1  # Reset

def solve_nqueens(N):
    board = [-1] * N
    solutions = [] 
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

def print_solutions(solutions, N):
    for sol in solutions:
        print("Solution:")
        for i in range(N):
            row = ['.'] * N 
            row[sol[i]] = 'Q'   
            print(' '.join(row))
        print() 

 
if __name__ == "__main__":
    N = int(input("Enter the number of queens: "))  
    solutions = solve_nqueens(N)  # Get all the solutions  

    print(f"Total solutions for {N}-Queens problem: {len(solutions)}")  # Print number of solutions
    print_solutions(solutions, N)
