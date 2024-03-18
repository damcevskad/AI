from constraint import *

def sudoku_constraint(a, b):
    return a != b

# Create a CSP problem
problem = Problem()

# Define variables (cells)
cells = []
for i in range(9):
    for j in range(9):
        cells.append((i, j))

# Add variables
for cell in cells:
    problem.addVariable(cell, range(1, 10))

# Define initial numbers on the Sudoku board
initial_numbers = [
    (0, 0, 5), (0, 1, 3), (0, 4, 7),
    (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
    (2, 1, 9), (2, 2, 8), (2, 7, 6),
    (3, 0, 8), (3, 4, 6), (3, 8, 3),
    (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
    (5, 0, 7), (5, 4, 2), (5, 8, 6),
    (6, 1, 6), (6, 6, 2), (6, 7, 8),
    (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
    (8, 0, 3), (8, 1, 7), (8, 2, 9), (8, 3, 4), (8, 5, 5), (8, 6, 6)
]

# Add initial numbers to the problem
for row, col, value in initial_numbers:
    problem.addConstraint(lambda cell, val=value: cell == val, ((row, col),))

# Add row, column, and subgrid constraints
for i in range(9):
    # Rows and columns
    row = [(i, j) for j in range(9)]
    col = [(j, i) for j in range(9)]
    problem.addConstraint(AllDifferentConstraint(), row)
    problem.addConstraint(AllDifferentConstraint(), col)
    
    # Subgrids
    subgrid = [(i//3*3 + k//3, i%3*3 + k%3) for k in range(9)]
    problem.addConstraint(AllDifferentConstraint(), subgrid)

# Solve the problem
solutions = problem.getSolutions()

# Print the solution(s)
if solutions:
    for solution in solutions:
        print(solution)
else:
    print("No solution found")