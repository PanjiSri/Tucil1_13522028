def find_combinations(matrix, buffer_size):
  """
  Mencari semua kombinasi susunan isi matriks di dalam buffer secara selang seling.

  Args:
    matrix: Matriks berukuran M x N.
    buffer_size: Panjang buffer yang sudah ditentukan dari awal.

  Returns:
    Array yang berisi kumpulan buffer yang sesuai dengan aturan.
  """

  m, n = len(matrix), len(matrix[0])
  # Inisialisasi buffer dan visited array.
  buffer = [None] * buffer_size
  visited = [[False for _ in range(n)] for _ in range(m)]

  # Menjalankan fungsi rekursif untuk mencari kombinasi.
  combinations = []
  _find_combinations(matrix, buffer, visited, 0, combinations)

  return combinations

def _find_combinations(matrix, buffer, visited, buffer_index, combinations):
  """
  Fungsi rekursif untuk mencari kombinasi susunan isi matriks di dalam buffer.

  Args:
    matrix: Matriks berukuran M x N.
    buffer: Buffer yang akan diisi dengan isi matriks.
    visited: Array yang menandakan apakah suatu titik matriks sudah dikunjungi.
    buffer_index: Indeks buffer saat ini.
    combinations: Array untuk menyimpan kombinasi yang ditemukan.
  """

  m, n = len(matrix), len(matrix[0])

  # Jika buffer sudah penuh, simpan kombinasi.
  if buffer_index == len(buffer):
    combinations.append(buffer.copy())
    return

  # Menentukan arah pengisian buffer berikutnya.
  direction = buffer_index % 2
  
  # Mencari semua kemungkinan titik untuk mengisi buffer.
  for i in range(m if direction else n):
    for j in range(n if direction else m):
      if not visited[i][j]:
        # Menandai titik sebagai dikunjungi.
        visited[i][j] = True

        # Mengisi buffer dengan isi matriks pada titik (i, j).
        buffer[buffer_index] = matrix[i][j]

        # Menjalankan fungsi rekursif untuk mencari kombinasi selanjutnya.
        _find_combinations(matrix, buffer, visited, buffer_index + 1, combinations)

        # Menandai titik sebagai tidak dikunjungi.
        visited[i][j] = False

# Contoh penggunaan
matrix = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"],
]
buffer_size = 3

combinations = find_combinations(matrix, buffer_size)

print("Output:")
for combination in combinations:
  print(combination)
