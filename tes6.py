
hasil = []

def cek(nilai, awal, arr=[]):
    global hasil
    if nilai == 1:
        print("ini basis")
        hasil.append(arr)
    else:
        if nilai == awal:
            arr = []
        arr.append(nilai)
        cek(nilai-1, awal, arr)

cek(5, 5)
print(hasil)
