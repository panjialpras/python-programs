#library 
import os

#Konversi Mata Uang
def idr_usd(nilai_tukar=14000):
    idr = float(input("Nominal IDR: "))
    usd = idr / nilai_tukar
    return round(usd, 0)

def usd_idr(nilai_tukar=14000):
    usd = float(input("Nominal USD: "))
    idr = usd * nilai_tukar
    return round(idr, 0)

#Program Utama
pilih = 0
while (pilih != 3):
    os.system("cls")    #membersihkan layar terminal (cmd)
    print("Program Konversi Uang IDR - USD")
    print("1. Konversi IDR ke USD")
    print("2. Konversi USD ke IDR")
    print("3. Keluar")
    pilih = int(input("Pilih menu: "))

    if (pilih == 1):
        print("Nilai tukar IDR ke USD adalah", idr_usd(15000))
    elif (pilih == 2):
        print("Nilai tukar USD ke IDR adalah", usd_idr(15000))
    elif (pilih == 3):
        print("Anda telah keluar")
    else:
        print("Menu yang dipilih tidak ada.")

    input()
