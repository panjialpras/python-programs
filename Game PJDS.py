#================================================================================
#Program Petani-Domba-Jagung-Serigala
#Pemain harus memindahkan petani, domba, jagung, dan serigala ke seberang sungai 
#menggunakan perahu yang hanya dapat memuat petani dan satu bawaan
#================================================================================
#import library
import os

#sub program (prosedur dan fungsi)
def tampil_gambar(list_kiri, list_kanan):
    print("Pindahkan Petani (P), Jagung (J), Domba (D), dan Serigala (S) ke sisi kanan!\n")

    #tampilkan objek pada list_kiri
    for item in list_kiri:
        print(item, end = " ")

    #cetak jarak
    print("\t\t\t", end = "")

    #tampilkan objek pada list_kanan
    for item in list_kanan:
        print(item, end = " ")

    #cetak daratan
    if ('P' in list_kiri):
        #jika petani 'P' ada di sisi kiri, maka perahu di sisi kiri
        print("\n======= \____/,,,,,,,,, ========")
    else:
        #jika petani 'P' ada di sisi kanan, maka perahu di sisi kanan
        print("\n======= ,,,,,,,,,\____/ ========")
    
def menyeberang(list_kiri, list_kanan):
    objek = input("\nSeberangkan (P, J, D, S): ")
    
    #konversi objek menjadi huruf kapital
    objek = objek.upper()

    #pindahkan objek dan petani 'P' dari sisi kiri ke sisi kanan jika keduanya ada di sisi kiri
    if (objek != 'P'):
        if (objek in list_kiri and 'P' in list_kiri):
            #hapus objek dan 'P' dari list_kiri
            list_kiri.remove(objek)
            list_kiri.remove('P')

            #tambahkan objek dan 'P' ke list_kanan
            list_kanan.append(objek)
            list_kanan.append('P')

        #pindahkan objek dan petani 'P' dari sisi kiri ke sisi kanan jika keduanya ada di sisi kiri
        elif (objek in list_kanan and 'P' in list_kanan):
            #hapus objek dan 'P' dari list_kanan
            list_kanan.remove(objek)
            list_kanan.remove('P')

            #tambahkan objek dan 'P' ke list_kiri
            list_kiri.append(objek)
            list_kiri.append('P')
        
        #beri peringatan jika petani 'P' dan objek tidak berada pada sisi yang sama
        else:
            print(objek, "yang ingin dipindahkan berseberangan dengan Petani 'P'!")
            input()
    else:
        if (objek in list_kiri):
            #hapus objek dan 'P' dari list_kiri
            list_kiri.remove(objek)

            #tambahkan objek dan 'P' ke list_kanan
            list_kanan.append(objek)

        #pindahkan objek dan petani 'P' dari sisi kiri ke sisi kanan jika keduanya ada di sisi kiri
        elif (objek in list_kanan):
            #hapus objek dan 'P' dari list_kanan
            list_kanan.remove(objek)

            #tambahkan objek dan 'P' ke list_kiri
            list_kiri.append(objek)

def cek_selesai(list_kiri, list_kanan):
    #kondisi jika semua objek P, J, D, S berada di sisi kanan semua
    if ('P' in list_kanan and 'J' in list_kanan and 'D' in list_kanan and 'S' in list_kanan):
        print("\nSELAMAT, Anda berhasil memindahkan keempatnya ke seberang!")
        input()
        return 1

    #kondisi jika J dan D berada di sisi kiri, sedangkan P di sisi kanan
    elif ('J' in list_kiri and 'D' in list_kiri and 'P' in list_kanan):
        print("\nOooppss, Anda gagal. Jagungnya habis dimakan Domba!")
        input()
        return 1
    
    #kondisi jika J dan D berada di sisi kanan, sedangkan P di sisi kiri
    elif ('J' in list_kanan and 'D' in list_kanan and 'P' in list_kiri):
        print("\nOooppss, Anda gagal. Jagungnya habis dimakan Domba!")
        input()
        return 1

    #kondisi jika D dan S berada di sisi kiri, sedangkan P di sisi kanan
    elif ('S' in list_kiri and 'D' in list_kiri and 'P' in list_kanan):
        print("\nOooppss, Anda gagal. Dombanya mati dimakan Serigala!")
        input()
        return 1

    #kondisi jika D dan S berada di sisi kiri, sedangkan P di sisi kanan
    elif ('S' in list_kanan and 'D' in list_kanan and 'P' in list_kiri):
        print("\nOooppss, Anda gagal. Dombanya mati dimakan Serigala!")
        input()
        return 1

    #kondisi lainnya (masih lanjut main)
    else:
        return 0

#program utama
os.system("cls")
list_kiri = ['P', 'J', 'D', 'S']
list_kanan = []
selesai = 0
main_lagi = 'Y'

tampil_gambar(list_kiri, list_kanan)

while (main_lagi.upper() == 'Y'):
    menyeberang(list_kiri, list_kanan)

    os.system("cls")
    tampil_gambar(list_kiri, list_kanan)

    selesai = cek_selesai(list_kiri, list_kanan)

    #jika selesai = True, tanya apakah mau main lagi atau tidak
    if (selesai == 1):
        main_lagi = input("\nMain lagi (Y/T)? ")

        #jika main_lagi = 'Y', reset lagi list_kiri dan list_kanan
        os.system("cls")
        list_kiri = ['P', 'J', 'D', 'S']
        list_kanan = []
        tampil_gambar(list_kiri, list_kanan)