#Variabel m untuk menyimpan matriks
#Berikut adalah matriks_dummy
m = [[1,2,3],[4,5,6],[7,8,9]]
baris = 3
kolom = 3

#koordinat
#x untuk baris dan y untuk kolom
x = 0
y = 0

#pembanding jumlah optimal
jumlah = 0
jumlah_sementara = 0

#buffer sebagai jumlah langkah maksimal
buffer = 2

#arah untuk memastikan penjumlahan hanya terjadi ketika terjadi perpindahan horizontal ke vertikal atau sebaliknya
arah = 0

#count dipake misal sekarang adalah untuk mengecek segala kemungkinan dengan i in range buffer, kalau count sudah sama dengan i, waktunya dibandingkan 
count = 0

for i in range(buffer):
    x = 0
    y = 0
    arah = 0  # inisialisasi di luar loop
    jumlah_sementara = 0
    count = 0
    for j in range(i+1):
        print("ini i:", i, " ini j:", j)
        if j % 2 == 0:
            while y < kolom:
                if arah == 1:
                    jumlah_sementara = 0
                    arah = 0
                    count = 0
                else:
                    jumlah_sementara += m[x][y]
                    count += 1
                    arah = 1
                    y += 1
                    if count >= i+1:
                        if (jumlah_sementara / i) > jumlah:
                            jumlah = jumlah_sementara
            y = 0

        else:
            while x < baris:
                # Proses serupa untuk perpindahan vertikal
                if arah == 1:
                    jumlah_sementara = 0
                    arah = 0
                    count = 0
                else:
                    jumlah_sementara += m[x][y]
                    count += 1
                    arah = 1
                    x += 1
                    if count >= i+1:
                        # Membandingkan total dengan langkah optimal
                        if jumlah_sementara > jumlah:
                            jumlah = jumlah_sementara

            x = 0  # reset x setelah iterasi vertikal