# matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
# buffer_size = 3

# m = len(matrix)
# n = len(matrix[0])

# visited = [[False] * n for _ in range(m)]     

# print(visited)       

# def is_valid_move(curr_pos, next_pos, visited):

#     m, n = len(visited), len(visited[0])

#     if (next_pos[0] < 0 or next_pos[0] >= m) or next_pos[1] < 0 or next_pos[1] >= n:
#         return False
#     if visited[next_pos[0]][next_pos[1]]:
#         return False  

#     return True

matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
buffer_size =3


#misal curr_pos itu terdiri dari 2 elemen
# x = curr_pos[0]
# y = curr_pos[1]

def is_titik_valid(matrix, visited, titik):
    baris = len(matrix)
    kolom = len(matrix[0])

    #Ini kalau titik gak ada di matrix
    if titik[0] < 0 or titik[0] >= baris or  titik[1] < 0 or titik[1] >= kolom:
        return False

    #Ini kalau dah dikunjungi
    if visited[titik[0]][titik[1]]:
        return False
    
    return True




    


# def find_move(matrix, direction, visited, titik):

#      arr_mov = []

#      if direction == 'V':




#def brute_force(matrix, buffer, titik, direction, visited):












    










# def bruteforce_matrix_combination(matrix, buffer_size):

#     result = []

#     def backtrack(path, curr_pos, visited):

#         if len(path) == buffer_size:

#             result.append(path.copy())

#             return
        

        