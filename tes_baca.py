def read_input(file_path):
    with open(file_path, 'r') as file:
        # Baca buffer_size
        buffer_size = int(file.readline().strip())

        # Baca ukuran matrix
        matrix_height, matrix_width = map(int, file.readline().strip().split())

        # Baca matrix
        matrix = [list(file.readline().strip().split()) for _ in range(matrix_height)]

        # Baca jumlah sequences
        num_sequences = int(file.readline().strip())

        # Inisialisasi array of sequences
        sequences = []

        # Baca sequences dan sequences_reward
        for _ in range(num_sequences):
            sequence = file.readline().strip().split()
            reward = int(file.readline().strip())
            sequences.append((sequence, reward))

    return buffer_size, matrix_width, matrix_height, matrix, sequences


# Contoh penggunaan
file_path = 'input.txt'  # Ganti dengan path file yang sesuai
buffer_size, matrix_width, matrix_height, matrix, sequences = read_input(file_path)

# Cetak hasil bacaan
print("Buffer Size:", buffer_size)
print("Matrix Width:", matrix_width)
print("Matrix Height:", matrix_height)
print("Matrix:")
for row in matrix:
    print(row)
print("Number of Sequences:", len(sequences))
for i, (sequence, reward) in enumerate(sequences, start=1):
    print(f"Sequence {i}: {sequence}, Reward: {reward}")
