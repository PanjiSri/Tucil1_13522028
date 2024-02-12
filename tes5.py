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
    global buffer_global
    if buffer == 1:
        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        # print('Ini Basis')
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        print(arr_kombinasi)
        list_kombinasi_global.append(arr_kombinasi.copy()) 
        arr_kombinasi.pop()

    else:
        # if buffer == buffer_global:
        #     arr_kombinasi = []
        
        arr_kombinasi.append(matriks[titik[0]][titik[1]])
        validasi[titik[0]][titik[1]] = True
            
        # print("ini arah", arah)

        #Nyari gerakan berikutnya
        list_move = find_move(arah, titik, matriks, validasi)

        print("Ini list_move", list_move)        
        if arah == 'V':
            arah_berikutnya = 'H'
        elif arah == 'H':
            arah_berikutnya = 'V'

        # print(arr_kombinasi)
        for titik_lanjutan in list_move:
            print("Ini titik lanjutan", titik_lanjutan)
            print("Ini buffer", buffer)
            bruteforce_combination(titik_lanjutan, buffer-1, arah_berikutnya, validasi, matriks, list_kombinasi_global, arr_kombinasi)
    
        arr_kombinasi.pop()

def origin_bruteforce_combination(matriks, buffer):

    baris = len(matriks)
    kolom = len(matriks[0])
    list_kombinasi_global = []
    for i in range(1):
        validasi = [[False for k in range(kolom)] for j in range(baris)]
        bruteforce_combination((0,i), buffer, 'V', validasi, matriks, list_kombinasi_global, [])

    print(list_kombinasi_global)

# Testing - Testing
buffer_global = 3
buffer_berubah = buffer_global


matriks = [['A','B','C'],
           ['D','E','F'],
           ['G','H','I']
           ]
buffer = 6

origin_bruteforce_combination(matriks, buffer)


#Ngecek origin_bruteforce_combination + bruteforce_combination



        

               
#Ngecek fungsi titik
# validasi = [[False, False],
#             [False, False],
#             [False, False]
#             ]
# titik = (1,1)
# arah = 'H'
# move = find_move(arah, titik, matriks, validasi)

# print(move)