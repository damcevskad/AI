from constraint import *  

# Create a CSP problem
problem = Problem() 

# Add variables
variables = range(0, 16)  # the variables are numbers from 0 to 15 (cells in the grid)
domain = range(1, 17)  #  the domain are the numbers from 1 to 16 to be placed on the grid
problem.addVariables(variables, domain)  #adding variables to the problem

# Add constraints
problem.addConstraint(AllDifferentConstraint(), variables)  # all variables must be different

# Adding row sum constraints
for row in range(4):
    problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)])

# Adding column sum constraints
for col in range(4):
    problem.addConstraint(ExactSumConstraint(34), [col + 4 * i for i in range(4)])

# Adding diagonal sum constraints
problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

# Solve the CSP
solution = problem.getSolution()  

# Print solution(s)
for solution in solutions:
    print(solution)