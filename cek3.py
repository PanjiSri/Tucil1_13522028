def generate_combinations(X, matrix, current_path, current_position):
    # Jika panjang path sama dengan X, tambahkan path ke matriks
    if len(current_path) == X:
        matrix.append(current_path.copy())
        return

    # Dapatkan posisi saat ini
    current_row, current_col = current_position

    # Tentukan semua kemungkinan langkah selanjutnya
    possible_moves = [
        (current_row, current_col + 1),  # Gerak horizontal
        (current_row + 1, current_col),  # Gerak vertikal
        (current_row, current_col - 1),  # Gerak horizontal mundur
        (current_row + 1, current_col + 1)  # Gerak diagonal
    ]

    for move in possible_moves:
        next_row, next_col = move

        # Periksa apakah posisi selanjutnya berada dalam batas matriks
        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
            # Pergi ke posisi selanjutnya
            generate_combinations(X, matrix, current_path + [matrix[next_row][next_col]], move)

# Fungsi untuk menghasilkan semua kombinasi
def generate_all_combinations(X, matrix):
    all_combinations = []
    for col in range(len(matrix[0])):
        generate_combinations(X, all_combinations, [matrix[0][col]], (0, col))
    return all_combinations

# Contoh penggunaan
X = 3
buffer_matrix = [
    ['7A', '55', 'E9'],
    ['55', '7A', '1C'],
    ['55', '1C', '1C']
]

result = generate_all_combinations(X, buffer_matrix)

# Menampilkan hasil
for combination in result:
    print(combination)
