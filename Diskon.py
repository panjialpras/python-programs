import math

print("----- Menghitung Diskon Sebuah Barang -----")

a = int(input("masukkan harga yang ingin ditentukan: "))

if (a >= 500000):
    harga = math.floor(a * 0.2)
    print('Anda mendapatkan diskon sebanyak 20% dan harga sekarang adalah Rp.', harga)
elif (a >= 300000):
    harga = math.floor(a * 0.1)
    print('Anda mendapatkan diskon sebanyak 10% dan harga sekarang adalah Rp.', harga)
elif (a >= 150000):
    harga = math.floor(a * 0.05)
    print('Anda mendapatkan diskon sebanyak 5% dan harga sekarang adalah Rp.', harga)
else:
    harga = print("Anda tidak mendapatkan diskon: ")
