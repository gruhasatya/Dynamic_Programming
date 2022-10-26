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



# Basic - 1
# Discuss tower of hanoi puzzle

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n - 1, auxiliary, destination, source)

n = 4
tower_of_hanoi(n, 'A', 'B', 'C')

# The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e.
# a disk can only be moved if it is the uppermost disk on a stack.
# 3. No disk may be placed on top of a smaller disk.

# Basic - 2
# Discuss N-Queen problem






















# Types of Analysis
# 1. Time Complexity    -   How much time does it take to run the algorithm
# 2. Space Complexity   -   How much space does it take to run the algorithm


# Time Complexity
# 1. Worst Case
# 2. Average Case
# 3. Best Case

######################################### lower bound - O(n) <= Average Time <= upper bound - O(n^2) #########################################

# Big O notation is used to describe the upper bound of an algorithm’s running time.
# Big Omega notation is used to describe the lower bound of an algorithm’s running time.
# Big Theta notation is used to describe the tight bound of an algorithm’s running time.

# Big O example
# O(n) + O(n) = O(n) + O(n) = O(n + n) = O(2n) = O(n)
# Ex - 1        f(n) = 3n + 8
# Ex - 2        f(n) = 3n^2 + 8n + 1


# Big Omega example
# Omega(n) + Omega(n) = Omega(n) + Omega(n) = Omega(n + n) = Omega(2n) = Omega(n)


# Big Theta example
# Theta(n) + Theta(n) = Theta(n) + Theta(n) = Theta(n + n) = Theta(2n) = Theta(n)


