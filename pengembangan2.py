#Buat nyari kemungkinan pergerakan, syarat : arah udah diketahui
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

#Rekursif buat nyari kombinasi
def bruteforce_combination(titik, buffer, arah, validasi, matriks, list_kombinasi_global, arr_kombinasi, koordinat, arr_koordniat):
    baris = len(matriks)
    kolom = len(matriks[0])

    if buffer == 1:

        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        arr_koordniat.append((titik[0],titik[1]))

        validasi[titik[0]][titik[1]] = True
        
        #print(validasi)

        validasi = [[False for k in range(kolom)] for j in range(baris)]

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

        arr_kombinasi.pop()
        arr_koordniat.pop()

def is_subarray(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            return True
    
    return False

def count_subarrays(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)
    count = 0

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            count += 1

    return count


#Buat nyari semua kombinasi untuk ukuran buffer tertentu
def origin_bruteforce_combination(matriks, buffer):

    baris = len(matriks)
    kolom = len(matriks[0])
    list_kombinasi_global = []
    koordinat = []

    for i in range(kolom):
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        bruteforce_combination((0,i), buffer, 'V', validasi, matriks, list_kombinasi_global, [], koordinat, [])

    return list_kombinasi_global, koordinat


def find_best_combines(matriks, buffer, matriks_sekuens):

    jumlah_pembanding = 0

    matriks_sekuens_terpilih = []

    list_kombinasi_global, list_koordinat = origin_bruteforce_combination(matriks, buffer)

    for kombinasi in list_kombinasi_global:
        # print(kombinasi)
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




# ukuran_buffer, kolom, baris, matrix, banyak_sekuens, arr_sekuens = read_input('input.txt')

# # print(ukuran_buffer)
# # print(kolom)
# # print(baris)
# # print(matrix)
# # print(banyak_sekuens)
# # print(arr_sekuens)


        

                
                
# matriks = [['A','B'],
#            ['D','E'],
#            ['I','K']
#            ]
# buffer = 4


# matriks_sekuens = [(['A', 'D', 'E'], 15), (['A', 'I', 'K'], 20), (['A','D','E','K'], 30)]

# print(find_best_combines(matriks, buffer, matriks_sekuens))

