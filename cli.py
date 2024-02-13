import random

def hasilkan_sekuens(tokens, jumlah_sekuens, ukuran_maksimal_sekuens):
    sekuens_unik = []

    def hasilkan_kombinasi(sekuens, sisa_ukuran):
        if sisa_ukuran == 0:
            nilai_acak = random.randint(-100, 100)
            sekuens_unik.append((sekuens[:], nilai_acak))  # Menambahkan salinan sekuens dan nilai acak ke sekuens_unik
            return
        for token in tokens:
            sekuens_baru = sekuens + [token]
            hasilkan_kombinasi(sekuens_baru, sisa_ukuran - 1)

    for panjang in range(2, ukuran_maksimal_sekuens + 1):
        hasilkan_kombinasi([], panjang)

    sekuens_terpilih = sekuens_unik[:jumlah_sekuens]

    return sekuens_terpilih


def hasilkan_matriks(tokens, jumlah_baris, jumlah_kolom):
    matriks = [['' for _ in range(jumlah_kolom)] for _ in range(jumlah_baris)]
    random.shuffle(tokens)
    indeks_token = 0

    for baris in range(jumlah_baris):
        for kolom in range(jumlah_kolom):
            matriks[baris][kolom] = tokens[indeks_token]
            indeks_token = (indeks_token + 1) % len(tokens)

    return matriks

def masukkan_CLI():
    jumlah_token = int(input("Masukkan banyak token: "))

    while True:
        token = input("Masukkan token (tolong pisahkan dengan spasi ya): ").split()
        if jumlah_token == len(token):
            break
        else:
            print("Jumlah token tidak sesuai")

    buffer = int(input("Masukkan ukuran buffer: "))

    kolom, baris = map(int, input("Masukkan ukuran matriks (format : kolom baris, contoh: 6 6): ").split())

    while True:
        jumlah_sekuens = int(input("Masukkan jumlah sekuens: "))
        ukuran_maksimal_sekuens = int(input("Masukkan ukuran maksimal sekuens: "))

        if jumlah_sekuens <= jumlah_token ** ukuran_maksimal_sekuens:
            break
        else:
            print("Jumlah Sekuens yang diminta melebihi jumlah maksimal sekuens yang dapat dibentuk. Silakan masukkan ulang.")

    sekuens = hasilkan_sekuens(token, jumlah_sekuens, ukuran_maksimal_sekuens)

    matrix = hasilkan_matriks(token, baris, kolom)
    return sekuens, matrix, buffer

sekuens , matrix, buffer = masukkan_CLI()

# print(sekuens)
# print(matrix)