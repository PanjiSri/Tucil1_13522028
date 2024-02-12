def is_valid_move(curr_pos, next_pos, visited):
    """
    Checks if a move from the current position to the next position is valid.

    Args:
        curr_pos: Current position (i, j)
        next_pos: Next position (i, j)
        visited: Visited nodes matrix

    Returns:
        True if the move is valid, False otherwise
    """

    m, n = len(visited), len(visited[0])

    if next_pos[0] < 0 or next_pos[0] >= m or next_pos[1] < 0 or next_pos[1] >= n:
        return False  # Out of bounds
    if visited[next_pos[0]][next_pos[1]]:
        return False  # Already visited
    return True

def bruteforce_matrix_combinations(matrix, buffer_size):
    """
    Finds all combinations of buffer_size moves in a matrix, starting from each cell.

    Args:
        matrix: Input matrix (list of lists)
        buffer_size: Maximum number of moves in a combination

    Returns:
        List of lists: All valid combinations with alternating moves
    """

    results = []

    def backtrack(path, curr_pos, visited):
        """
        Performs backtracking to explore and collect valid combinations.

        Args:
            path: Current combination path (list of cells)
            curr_pos: Current position (i, j)
            visited: Visited nodes matrix
        """

        if len(path) == buffer_size:
            results.append(path.copy())  # Append a copy to avoid modifications
            return

        # Possible directions for alternating moves
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            next_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])

            if is_valid_move(curr_pos, next_pos, visited):
                visited[next_pos[0]][next_pos[1]] = True
                path.append(matrix[next_pos[0]][next_pos[1]])

                backtrack(path, next_pos, visited)  # Explore further

                visited[next_pos[0]][next_pos[1]] = False
                path.pop()  # Backtrack and remove last step

    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            visited = [[False] * n for _ in range(m)]
            visited[i][j] = True
            path = [matrix[i][j]]
            backtrack(path, (i, j), visited)

    return results

# Example usage:
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
buffer_size = 3

combinations = bruteforce_matrix_combinations(matrix, buffer_size)
print(combinations)
