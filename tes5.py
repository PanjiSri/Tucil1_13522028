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


#Ngecek fungsi titik
matriks = [['A','B'],
           ['C','D'],
           ['E','F']
           ]
validasi = [[False, False],
            [False, False],
            [False, False]
            ]
titik = (1,1)
arah = 'H'
move = find_move(arah, titik, matriks, validasi)

print(move)