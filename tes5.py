def find_move(arah, titik, matriks, validasi):
    baris = len(matriks)
    kolom = len(matriks)
    move = []
    if arah == 'V':
        for i in range(kolom):
            if validasi[i][titik[1]] == False and (i, titik[1]) != titik:
                move.append((i,titik[1]))
    elif arah == 'H':
        for j in range(baris):
            if validasi[titik[0]][j] == False and (titik[0], j) != titik:
                move.append((titik[0],j))
    return move