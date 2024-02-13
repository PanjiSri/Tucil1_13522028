"""
Tugas Kecil 1 IF2211 Strategi Algoritma
Semester II tahun 2023/2024
Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force
"""

"""
PANJI SRI KUNCARA WISMA - 13522028
"""

import os
import random
import time

#Fungsi ini dipake buat nentuin arah gerak
def find_move(arah, titik, matriks, validasi):
    baris = len(matriks)
    kolom = len(matriks[0])
    move = []
    if arah == 'V':
        for i in range(baris):
            if validasi[i][titik[1]] == False and (i, titik[1]) != titik:
                move.append((i,titik[1]))
    elif arah == 'H':
        for j in range(kolom):
            #print("ini j", j)
            if validasi[titik[0]][j] == False and (titik[0], j) != titik:
                move.append((titik[0],j))
    return move


#Fungsi Rekursif buat nyari kombinasi isi matriks sekaligus titik koordinatnya
def bruteforce_combination(titik, buffer, arah, validasi, matriks, list_kombinasi_global, arr_kombinasi, koordinat, arr_koordniat):
    baris = len(matriks)
    kolom = len(matriks[0])

    if buffer == 1:

        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        arr_koordniat.append((titik[0],titik[1]))

        validasi[titik[0]][titik[1]] = True
        
        #print(validasi)

        #validasi = [[False for k in range(kolom)] for j in range(baris)]

        list_kombinasi_global.append(arr_kombinasi.copy()) 
        koordinat.append(arr_koordniat.copy())

        arr_kombinasi.pop()
        arr_koordniat.pop()

    else:
        
        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        arr_koordniat.append((titik[0],titik[1]))

        validasi[titik[0]][titik[1]] = True
            
        list_move = find_move(arah, titik, matriks, validasi)

        #print(validasi)

        if arah == 'V':
            arah_berikutnya = 'H'
        elif arah == 'H':
            arah_berikutnya = 'V'

        for titik_lanjutan in list_move:

            bruteforce_combination(titik_lanjutan, buffer-1, arah_berikutnya, validasi, matriks, list_kombinasi_global, arr_kombinasi, koordinat, arr_koordniat)
            # validasi = [[False for k in range(kolom)] for j in range(baris)]
            validasi[titik_lanjutan[0]][titik_lanjutan[1]] = False

        arr_kombinasi.pop()
        arr_koordniat.pop()

#Pintu gerbang buat masuk fungsi rekursif bruteforce_combination
def origin_bruteforce_combination(matriks, buffer):

    baris = len(matriks)
    kolom = len(matriks[0])
    list_kombinasi_global = []
    koordinat = []

    for i in range(kolom):
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        bruteforce_combination((0,i), buffer, 'V', validasi, matriks, list_kombinasi_global, [], koordinat, [])

    return list_kombinasi_global, koordinat

#Fungsi ini dipake buat ngecek apakah suatu array itu ada di array yang lain
def is_subarray(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            return True
    
    return False

#Fungsi ini dipake buat ngecek ada berapa banyak suatu array yang ada di array yang lain
def count_subarrays(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)
    count = 0

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            count += 1

    return count

#Buat nyari langkah terbaik
def find_best_combines(matriks, buffer, matriks_sekuens):

    jumlah_pembanding = 0

    matriks_sekuens_terpilih = []

    list_kombinasi_global = []

    list_koordinat = []

    for i in range(1, buffer+1):

        list_kombinasi_global_sementara, list_koordinat_sementara = origin_bruteforce_combination(matriks, i)

        list_kombinasi_global.extend(list_kombinasi_global_sementara.copy())
        list_koordinat.extend(list_koordinat_sementara.copy())

        list_kombinasi_global_sementara = []
        list_koordinat_sementara = []

    # for i in list_kombinasi_global:
    #     if(i[0] == '7A'):
    #         print(i)

    for kombinasi in list_kombinasi_global:
        jumlah_sementara = 0
        for sekuens in matriks_sekuens:
            #print(sekuens)
            if is_subarray(sekuens[0], kombinasi):
                count = count_subarrays(sekuens[0],kombinasi)
                temp = count * sekuens[1]
                jumlah_sementara = jumlah_sementara + temp

        if jumlah_sementara > jumlah_pembanding:
                # print(kombinasi, jumlah_sementara)
            jumlah_pembanding = jumlah_sementara
            matriks_sekuens_terpilih = kombinasi
    
    if matriks_sekuens_terpilih != []:
        index = list_kombinasi_global.index(matriks_sekuens_terpilih)
        langkah_koordinat = list_koordinat[index]
    else:
        langkah_koordinat = []

    return matriks_sekuens_terpilih, jumlah_pembanding, langkah_koordinat


def read_input(file_path):

    file_path = os.path.join('..', file_path)

    with open(file_path, 'r') as file:

        #ukuran buffer
        ukuran_buffer = int(file.readline().strip())

        # kolom
        kolom, baris = map(int, file.readline().strip().split())

        #matrix
        matrix = [list(file.readline().strip().split()) for _ in range(baris)]

        #banyak sekuens
        banyak_sekuens = int(file.readline().strip())

        arr_sekuens = []

        for _ in range(banyak_sekuens):
            sekuens = file.readline().strip().split()
            reward = int(file.readline().strip())
            arr_sekuens.append((sekuens, reward))
            
    return ukuran_buffer, kolom, baris, matrix, banyak_sekuens, arr_sekuens


#Generate Sekuens
def hasilkan_sekuens(tokens, jumlah_sekuens, ukuran_maksimal_sekuens):
    sekuens_unik = []

    def hasilkan_kombinasi(sekuens, sisa_ukuran):
        if sisa_ukuran == 0:
            nilai_acak = random.randint(-100, 100)
            sekuens_unik.append((sekuens[:], nilai_acak))  
            return
        for token in tokens:
            sekuens_baru = sekuens + [token]
            hasilkan_kombinasi(sekuens_baru, sisa_ukuran - 1)

    for panjang in range(2, ukuran_maksimal_sekuens + 1):
        hasilkan_kombinasi([], panjang)

    sekuens_terpilih = sekuens_unik[:jumlah_sekuens]

    return sekuens_terpilih

#Generate Matriks
def hasilkan_matriks(tokens, jumlah_baris, jumlah_kolom):
    matriks = [['' for _ in range(jumlah_kolom)] for _ in range(jumlah_baris)]
    random.shuffle(tokens)
    indeks_token = 0

    for baris in range(jumlah_baris):
        for kolom in range(jumlah_kolom):
            matriks[baris][kolom] = tokens[indeks_token]
            indeks_token = (indeks_token + 1) % len(tokens)

    return matriks

#Masukkan via CLI
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
    return matrix, buffer, sekuens

#kode buat nulis file
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def main():
    print("Tucil 1 STIMA")
    while True:
        print("Pilih salah satu")
        print("1. Masukkan Via CLI")
        print("2. Masukkan Via Input Text")
        masukkan = input("Tuliskan Angka Pilihan (1 atau 2): ")

        if masukkan == '1' or masukkan == '2':
            break
        else:
            print("Tolong inputkan dengan benar")
            
    if (masukkan == '1'):
        matriks, buffer, sekuens = masukkan_CLI()

        start_time = time.time()
        matriks_sekuens_terpilih, jumlah_pembanding, langkah_koordinat = find_best_combines(matriks, buffer, sekuens)
        end_time = time.time()

        print("----------------Ini Matriksnya-----------------")
        for i in range(len(matriks)):
            for j in range(len(matriks[0])):
                print(f"{matriks[i][j]}", end=" ")
            print()

        print("----------------Ini sekuensnya------------------")
        for sekuens in sekuens:
            for j in sekuens[0]:
                print(j, end=" ")
            print()
            print("bobot: ",sekuens[1])
        print("----------------Ini buffer------------------")
        print("Ukuran Buffer= ", buffer)
        print("----------------Solusi------------------")
        print(jumlah_pembanding)

        for i in matriks_sekuens_terpilih:
            print(i, end=" ")
        print()

        result = [(y+1, x+1) for x, y in langkah_koordinat]

        for point in result:
            print(f"{point[0]}, {point[1]}")

        elapsed_time = end_time - start_time
        print()
        print(f"{elapsed_time * 1000:.2f} ms")
        print()


        save_solution = input("Apakah ingin menyimpan solusi? (y/n): ").lower()

        if save_solution == 'y':
            filename = input("Masukkan nama file (termasuk ekstensi .txt): ")

            content = f"{jumlah_pembanding}\n"
            content += ' '.join(map(str, matriks_sekuens_terpilih)) + '\n'
            content += '\n'.join([f"{x[0]}, {x[1]}" for x in result]) + '\n'
            content += "\n"
            content += f"{elapsed_time * 1000:.2f} ms\n"
    
     
            file_path = os.path.join('..', 'test', filename)
            write_to_file(file_path, content)
            print(f"Hasil telah ditulis ke dalam file {filename}")
        else:
            print("Solusi tidak disimpan.")


    else:
        print("\n-----Pastikan file sudah ada dan berada sejajar di path yang sama dengan folder src, doc, bin, dan test-----\n")

        file_path = input("Masukkan nama file dan extensinya (contoh: input.txt): ")

        buffer, kolom, baris, matriks, banyak_sekuens, sekuens = read_input(file_path)

        start_time = time.time()
        matriks_sekuens_terpilih, jumlah_pembanding, langkah_koordinat = find_best_combines(matriks, buffer, sekuens)
        end_time = time.time()

        print(jumlah_pembanding)

        for i in matriks_sekuens_terpilih:
            print(i, end=" ")
        print()

        result = [(y+1, x+1) for x, y in langkah_koordinat]

        for point in result:
            print(f"{point[0]}, {point[1]}")

        elapsed_time = end_time - start_time
        print()
        print(f"{elapsed_time * 1000:.2f} ms")
        print()


        save_solution = input("Apakah ingin menyimpan solusi? (y/n): ").lower()

        if save_solution == 'y':
            filename = input("Masukkan nama file (termasuk ekstensi .txt): ")

            content = f"{jumlah_pembanding}\n"
            content += ' '.join(map(str, matriks_sekuens_terpilih)) + '\n'
            content += '\n'.join([f"{x[0]}, {x[1]}" for x in result]) + '\n'
            content += "\n"
            content += f"{elapsed_time * 1000:.2f} ms\n"
    
     
            file_path = os.path.join('..', 'test', filename)
            write_to_file(file_path, content)
            print(f"Hasil telah ditulis ke dalam file {filename}")
        else:
            print("Solusi tidak disimpan.")


if __name__ == "__main__":
    main()


