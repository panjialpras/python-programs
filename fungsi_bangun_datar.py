#library
import os

#Program Bangun Datar
def keliling(panjang, lebar):     #p dan l adalah parameter formal
    K = 2 * (panjang + lebar)
    return K
    
def luas(panjang, lebar):
    L = panjang * lebar
    return L

def volume():
    panjang = int(input("Panjang: "))
    lebar = int(input("Lebar: "))
    tinggi = int(input("Tinggi: "))
    V = panjang * lebar * tinggi
    return V

#Program Utama
pilih = 0
while (pilih != 4):
    os.system("cls")
    print("Program Menghitung Keliling dan Luas Bangun Datar")
    print("1. Keliling Persegi Panjang")
    print("2. Luas Persegi Panjang")
    print("3. Volume Balok")
    print("4. Keluar")
    pilih = int(input("Pilih menu: "))

    if (pilih == 1):
        panjang = int(input("Panjang: "))
        lebar = int(input("Lebar: "))
        print("Keliling Persegi Panjang =", keliling(panjang, lebar))
    elif (pilih == 2):
        panjang = int(input("Panjang: "))
        lebar = int(input("Lebar: "))
        print("Luas Persegi Panjang =", luas(panjang, lebar))
    elif (pilih == 3):
        print("Volume Balok =", volume())
    elif (pilih == 4):
        print("Anda telah keluar")
    else:
        print("Menu yang dipilih tidak tersedia.")
    
    input()

