def is_valid_move(curr_pos, next_pos, visited):
    if next_pos[0] < 0 or next_pos[0] >= len(visited) or next_pos[1] < 0 or next_pos[1] >= len(visited[0]):
        return False
    if visited[next_pos[0]][next_pos[1]]:
        return False
    return True

def bruteforce_matrix_combinations(matrix, buffer_size):
    result = []

    def backtrack(path, curr_pos, visited):
        if len(path) == buffer_size:
            result.append(path.copy())
            return

        # Possible directions for alternating moves
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            next_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])

            if is_valid_move(curr_pos, next_pos, visited):
                visited[next_pos[0]][next_pos[1]] = True
                path.append(matrix[next_pos[0]][next_pos[1]])

                backtrack(path, next_pos, visited)

                visited[next_pos[0]][next_pos[1]] = False
                path.pop()

    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            visited = [[False] * n for _ in range(m)]
            visited[i][j] = True
            path = [matrix[i][j]]
            backtrack(path, (i, j), visited)

    return result

# Example usage:
matrix_3x3 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
buffer_size = 3

result = bruteforce_matrix_combinations(matrix_3x3, buffer_size)
print(result)
