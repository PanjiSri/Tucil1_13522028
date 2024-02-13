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

        # print("Ini list move")
        # print(list_move)

        for titik_lanjutan in list_move:
            bruteforce_combination(titik_lanjutan, buffer-1, arah_berikutnya, validasi, matriks, list_kombinasi_global, arr_kombinasi, koordinat, arr_koordniat)
            validasi = [[False for k in range(kolom)] for j in range(baris)]

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

    for i in list_kombinasi_global:
        if i[0] == '7A':
            print(i)

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
                
                
matriks = [['7A', '55', 'E9', 'E9', '1C', '55'], 
           ['55', '7A', '1C', '7A', 'E9', '55'], 
           ['55', '1C', '1C', '55', 'E9', 'BD'], 
           ['BD', '1C', '7A', '1C', '55', 'BD'], 
           ['BD', '55', 'BD', '7A', '1C', '1C'], 
           ['1C', '55', '55', '7A', '55', '7A']]

#matriks = [['A','B','C'],['D','E','F'],['G','H','I']]
buffer = 6

origin_bruteforce_combination(matriks, buffer)

# matriks_sekuens = [(['BD', 'E9', '1C'], 15), (['BD', '7A', 'BD'], 20), (['BD','1C','BD','55'], 30)]

# print(find_best_combines(matriks, buffer, matriks_sekuens))