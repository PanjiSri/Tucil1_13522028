matriks = [ ['7A', '55', 'E9', 'E9', '1C', '55'],
            ['55', '7A', '1C', '7A', 'E9', '55'],
            ['55', '1C', '1C', '55', 'E9', 'BD'],
            ['BD', '1C', '7A', '1C', '55', 'BD'],
            ['BD', '55', 'BD', '7A', '1C', '1C'],
            ['1C', '55', '55', '7A', '55', '7A']]


sekuens1 = ['BD','E9','1C']
sekuens2 = ['BD','7A','BD']
sekuens3 = ['BD','1C','BD','55']

#berurutan bobot sekuens 1, 2, dan 3
bobot = [15,20,30]

#langkah
buffer = 1

#total nilai
jumlah = 0

kolom = 1
counter = 0

def is_subarray(subarray, array):
    len_subarray = len(subarray)
    len_array = len(array)

    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            return True

    return False


def cari_solusi(baris, matriks, sekuens1, sekuens2, sekuens3, bobot, buffer, counter, kolom, jumlah):

    jumlah_sementara = 0

    if counter >= kolom:

        print("berhenti")
    
    else:

        for i in range(buffer):
                
            matriks_mungkin = []

            for j in range(i+1):
                
                x = 0

                y = 0

                if (j % 2) == 0:


                    while x < baris:



                        x += 1

                    



                # cek = 0

                # x = 0
                # y = 0
                # arr_mungkin = []

                # if j == 0:

                #     arr_mungkin.append(matriks[0][counter])

                #     x += 1

                # while x < baris:
                    
                #     while y < kolom:

                #         if j % 2 == 0:

                #             arr_mungkin.append(matriks[x][y])


                #             x += 1

                #             cek += 1
                        
                #         else:

                #             arr_mungkin.append(matriks[x][y])

                #             y += 1

                #             cek += 1

                        
                #         if cek >= i+1:

                #             cek = 0

                #             if is_subarray(arr_mungkin, sekuens1):

                #                 jumlah_sementara += bobot[0]
                                
                #             if is_subarray(arr_mungkin, sekuens2):

                #                 jumlah_sementara += bobot[1]

                #             if is_subarray(arr_mungkin, sekuens3):

                #                 jumlah_sementara += bobot[2]

                #             if jumlah_sementara > jumlah:

                #                 jumlah = jumlah_sementara
                            
                #             arr_mungkin = []
                            
                            

                    
                            
        counter += 1

    cari_solusi(baris, matriks, sekuens1, sekuens2, sekuens3, bobot, buffer, counter, kolom, jumlah)        




    



