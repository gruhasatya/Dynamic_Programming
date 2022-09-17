# Recursion and BackTracking
# recursion is a function that calls itself
# Backtracking is a method of solving a problem by exploring all possible candidates for the solution
# Backtracking to the last valid state when no more candidates can be found.


# there are two types of problems in backtracking
# Decision Problem – In this, we search for a feasible solution.
# Optimization Problem – In this, we search for the best solution.
# Enumeration Problem – In this, we find all feasible solutions.



# Consider a situation that you have three boxes in front of you and only one of them has a gold coin in it
# but you do not know which one. So, in order to get the coin, you will have to open all of the boxes one by one.
# You will first check the first box, if it does not contain the coin, you will have to close it and check the second box
# and so on until you find the coin. This is what backtracking is, that is solving all sub-problems one by one in order to reach the best possible solution.


# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems,
# that incrementally builds candidates to the solutions, and abandons each partial candidate (“backtracks”)
# as soon as it determines that the candidate cannot possibly be completed to a valid solution.



####################################################################### Recursive Backtracking Algorithm #######################################################################



# def solution(n, other_sol):
#     if (found a solution):
#         solutionfound += 1
#         print(solution)
#         if (solutionFound >= solutionTarget):
#             system.exit()
#         return 0
#     for value = first to  last:
#         if (value is a valid choice):
#             add value to the solution
#             solution(n+1, other_sol)
#             remove value from the solution

# chess = 8*8

# Constraints
# 1. Can not traverse the same cell twice
# 2. Can not move outside the board

# from one point you can reach till 8 points
# 1. 2 steps forward and 1 step to the right
# 2. 2 steps forward and 1 step to the left
# 3. 1 step forward and 2 steps to the right
# 4. 1 step forward and 2 steps to the left
# 5. 2 steps backward and 1 step to the right
# 6. 2 steps backward and 1 step to the left
# 7. 1 step backward and 2 steps to the right
# 8. 1 step backward and 2 steps to the left


def CanWeMove(board, visited, row, col):                                                        # Check if we can move to the next cell
    if row >= 0 and row < 8 and col >= 0 and col < 8 and visited[row][col] == 0:                # Check if the cell is inside the board and not visited
        return True
    return False

def KnightTour(board, visited, row, col, move):                                                 # Recursive function to solve the problem
    if move == 64:                                                                              # If all the cells are visited Return True
        return True
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]                                                        # Possible moves of the Knight
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):                                                                          # Try all the possible moves
        nextX = row + xMove[i]                                                                  # Get the next move
        nextY = col + yMove[i]
        if CanWeMove(board, visited, nextX, nextY):                                             # Check if the move is valid
            visited[nextX][nextY] = move                                                        # Mark the cell as visited
            if KnightTour(board, visited, nextX, nextY, move + 1):                              # Recursively call the function and increment the move to check for next 8 moves
                return True
            visited[nextX][nextY] = 0                                                           # If the move is not valid then backtrack and mark the cell as unvisited
    return False

def KnightTourMain():                                                                          # Main function to solve the problem
    board = [[0 for i in range(8)] for j in range(8)]                                          # Create a board of 8*8
    visited = [[0 for i in range(8)] for j in range(8)]                                        # Create a visited array of 8*8
    visited[0][0] = 1                                                                          # Mark the first cell as visited
    if KnightTour(board, visited, 0, 0, 1):                                                    # Call the recursive function
        print("Solution exists")
    else:
        print("Solution does not exist")

KnightTourMain()

# The Knight’s tour problem is a famous problem in computer science and mathematics.
