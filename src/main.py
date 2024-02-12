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

def bruteforce_combination(titik, buffer, arah, validasi, matriks, list_kombinasi_global, arr_kombinasi):
    baris = len(matriks)
    kolom = len(matriks[0])

    if buffer == 1:

        arr_kombinasi.append(matriks[titik[0]][titik[1]])

        validasi[titik[0]][titik[1]] = True
        
        #print(validasi)

        validasi = [[False for k in range(kolom)] for j in range(baris)]

        list_kombinasi_global.append(arr_kombinasi.copy()) 

        arr_kombinasi.pop()

    else:
        
        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        validasi[titik[0]][titik[1]] = True
            
        list_move = find_move(arah, titik, matriks, validasi)

        #print(validasi)

        if arah == 'V':
            arah_berikutnya = 'H'
        elif arah == 'H':
            arah_berikutnya = 'V'

        for titik_lanjutan in list_move:

            bruteforce_combination(titik_lanjutan, buffer-1, arah_berikutnya, validasi, matriks, list_kombinasi_global, arr_kombinasi)

        arr_kombinasi.pop()


def origin_bruteforce_combination(matriks, buffer):

    baris = len(matriks)
    kolom = len(matriks[0])
    list_kombinasi_global = []

    for i in range(kolom):
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        bruteforce_combination((0,i), buffer, 'V', validasi, matriks, list_kombinasi_global, [])

    print(list_kombinasi_global)


# TESS
matriks = [['A','B','C'],
           ['D','E','F'],
           ['G','H','I']
           ]
buffer = 4

origin_bruteforce_combination(matriks, buffer)