import os

def clear () :
    os.system("cls")

def ulang () :
    ulang = str(input("Ingin menghitung lagi? y/n : "))
    if ulang == "y":
        menu ()
    else :
        "Anda telah keluar"

def persegi (a, b) :
    x = a * b
    print ("Hasil", x)
    ulang ()
def segitiga (c, a, b) :
    y = 1/2 * a * b
    print ("Hasil", y)
    ulang ()
def lingkaran (c, a, b) :
    z = 22/7 * a * b
    print ("Hasil", z)
    hasil = a + b + z / 3
    ulang()


def menu () :
    clear ()
    a = int(input("Masukkan angka pertama : "))
    b = int(input("Masukkan angka kedua : "))
    print ("Program menghitung ketiga bangun datar dan rata-ratanya")
    print ("1. Persegi")
    print ("2. Segitiga")
    print ("3. Lingkaran")
    print ("4. Keluar program")
    menu = int(input("Pilihlah menu yang ingin anda hitung : "))
    if (menu == 1) :
        persegi(a,b)
    elif (menu == 2) :
        segitiga(1/2,a,b)
    elif (menu == 3) :
        lingkaran(22/7,a,b)
    else:
        print("anda telah keluar program")
menu ()