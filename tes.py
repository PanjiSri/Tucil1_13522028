def hasilkan_sekuens(tokens, jumlah_sekuens, ukuran_maksimal_sekuens):
    sekuens_unik = set()

    def hasilkan_kombinasi(sekuens, sisa_ukuran):
        if sisa_ukuran == 0:
            sekuens_unik.add(' '.join(sekuens))
            return
        for token in tokens:
            sekuens_baru = sekuens + [token]
            hasilkan_kombinasi(sekuens_baru, sisa_ukuran - 1)

    for panjang in range(2, ukuran_maksimal_sekuens + 1):
        hasilkan_kombinasi([], panjang)

    sekuens_terpilih = list(sekuens_unik)[:jumlah_sekuens]

    return sekuens_terpilih

jumlah_token_unik = int(input("Masukkan Jumlah Token Unik: "))
token = input("Masukkan Token (pisahkan dengan spasi): ").split()
jumlah_sekuens = int(input("Masukkan Jumlah Sekuens: "))
ukuran_maksimal_sekuens = int(input("Masukkan Ukuran Maksimal Sekuens: "))

if jumlah_sekuens > jumlah_token_unik ** ukuran_maksimal_sekuens:
    print("Jumlah Sekuens yang diminta melebihi jumlah maksimal sekuens yang dapat dibentuk.")
else:
    hasil = hasilkan_sekuens(token, jumlah_sekuens, ukuran_maksimal_sekuens)
    for idx, seq in enumerate(hasil, start=1):
        print(f"{idx}. {seq}")


import random

def generate_matrix(tokens, matrix_size):
    matrix = []
    
    for _ in range(matrix_size):
        row = random.choices(tokens, k=matrix_size)
        matrix.append(row)
    
    return matrix

# Input
jumlah_token = int(input("Masukkan Banyak Token: "))
token_input = input("Masukkan Token (pisahkan dengan spasi): ").split()
ukuran_matriks = int(input("Masukkan Ukuran Matriks: "))

# Mengecek apakah jumlah token sesuai dengan yang diinputkan
if jumlah_token != len(token_input):
    print("Jumlah token tidak sesuai dengan yang diinputkan.")
else:
    # Menghasilkan matriks
    matriks = generate_matrix(token_input, ukuran_matriks)

    # Menampilkan matriks
    print("\nMatriks Hasil:")
    for row in matriks:
        print(" ".join(row))
