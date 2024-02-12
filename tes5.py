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

buffer_global = 3
buffer_berubah = buffer_global

def bruteforce_combination(titik, buffer, arah, validasi, matriks):
    baris = len(matriks)
    kolom = len(matriks[0])
    global buffer_global
    if buffer == 1:
        print('Ini Basis')
        validasi = [[False for k in range(kolom)] for j in range(baris)]
    else:
        if buffer == buffer_global:
            arr_kombinasi = []
            arr_kombinasi.append(matriks[titik[0]][titik[1]])
            validasi[titik[0]][titik[1]] = True
        else:
            arr_kombinasi.append(matriks[titik[0]][titik[1]])
            validasi[titik[0]][titik[1]] = True
            
            #Nyari gerakan berikutnya
            list_move = find_move(arah, titik, matriks, validasi)

            if arah == 'V':
                arah_berikutnya = 'H'
            elif arah == 'H':
                arah_berikutnya = 'V'
            
            for titik_lanjutan in list_move:
                bruteforce_combination(titik_lanjutan, buffer-1, arah_berikutnya, validasi, matriks)

def origin_bruteforce_combination(matriks, buffer):

    baris = len(matriks)
    kolom = len(matriks[0])
    for i in range(kolom):
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        bruteforce_combination((0,i), buffer, 'V', validasi, matriks)




            
        
        







#Ngecek fungsi titik
# matriks = [['A','B'],
#            ['C','D'],
#            ['E','F']
#            ]
# validasi = [[False, False],
#             [False, False],
#             [False, False]
#             ]
# titik = (1,1)
# arah = 'H'
# move = find_move(arah, titik, matriks, validasi)

# print(move)