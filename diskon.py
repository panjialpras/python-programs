print ("----- Menghitung Diskon Sebuah Barang -----")

a = int(input("masukkan harga yang ingin ditentukan: "))

if (a >= 500000) :
    harga = a * 0.2
elif (a >= 300000) :
    harga = a * 0.1
elif (a >= 150000) :
    harga = a * 0.05
else:
    harga = print("Anda tidak mendapatkan diskon: ")

print(harga)