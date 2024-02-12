def generate_combinations(matrix, buffer_size, path, i, j, result):
    # Base case: jika buffer_size mencapai 0, simpan path ke dalam result
    if buffer_size == 0:
        result.append(path.copy())
        return

    # Tambahkan elemen saat ini ke dalam path
    path.append(matrix[i][j])

    # Simpan posisi saat ini
    temp_i, temp_j = i, j

    # Bergerak ke atas (vertikal) jika mungkin
    if i - 1 >= 0:
        generate_combinations(matrix, buffer_size - 1, path, i - 1, j, result)

    # Bergerak ke kanan (horizontal) jika mungkin
    i, j = temp_i, temp_j
    if j + 1 < len(matrix[0]):
        generate_combinations(matrix, buffer_size - 1, path, i, j + 1, result)

    # Hapus elemen terakhir dari path untuk backtracking
    path.pop()

# Contoh penggunaan
matrix = [['A', 'B'], ['C', 'D']]
buffer_size = 3
result = []

# Iterasi melalui setiap elemen di baris pertama untuk memulai pergerakan
for j in range(len(matrix[0])):
    generate_combinations(matrix, buffer_size, [], 0, j, result)

# Print hasil kombinasi
for combination in result:
    print(combination)
