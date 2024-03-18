from search import Problem, depth_first_tree_search, breadth_first_tree_search
# from notebook import plot_NQueens

class NQueensPuzzle(Problem):

    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of -1 means that the c-th column has not been
    filled in yet.  We fill in columns left to right.
    >>> depth_first_tree_search(NQueensProblem(8))
    <Node (7, 3, 0, 2, 5, 1, 6, 4)>
    """

    def __init__(self, N):
        self.N = N
        self.initial = tuple([-1] * N)
        Problem.__init__(self, self.initial)

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] is not -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)   # same / diagonal

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] is -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))
    
    def print_board(state):
        for row in range(len(state)):
            for col in range(len(state)):
                if state[col] == row:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print()


if __name__ == '__main__':
        nqp = NQueensPuzzle(8)
        result1 = depth_first_tree_search(nqp)
        print("\n Depth First Search Solution:")
        print(result1.solution())
        nqp.print_board(solution1)
        # plot_NQueens(result1.solution())

        result2 = breadth_first_tree_search(nqp)
        print("\n Breadth First Search Solution:")
        print(result2.solution())
        nqp.print_board(solution2)
        # plot_NQueens(result2.solution())