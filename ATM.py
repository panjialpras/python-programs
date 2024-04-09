import os

identitas = ["No rekening 5200411249", "Nama : Panji"]
air = [int(input("masukkan no seri : ",))]
rekening_tujuan = ["No rek.", 9348578935, "Nama : Aldi", "Bank BRI"]

isi_ATM = 3500000


def clear():
    os.system("cls")


def cek():
    print("Saldo anda pada ATM adalah: ", isi_ATM)


def tarik():
    tarik_uang = isi_ATM - (int(input("Masukkan jumlah penarikan : ")))
    if tarik_uang > isi_ATM:
        print('Saldo tidak mencukupi')
        return 0
    else:
        return tarik_uang


def transfer():
    no_rek = input("masukkan nomor rekening : ")
    nama = input("masukkan nama penerima transfer tujuan : ")
    transfer = int(input("Masukkan jumlah  transfer : "))
    if transfer > isi_ATM:
        print("Maaf, saldo tidak mencukupi.")
        return 0
    else:
        print(no_rek, nama, transfer)
        print("--------------------------")
        print(identitas, "Rp.", transfer)
        print("Transfer berhasil!")
        return transfer


def bayar_listrik_air():
    tagihan = 350000
    if tagihan > isi_ATM:
        print("Maaf, saldo tidak mencukupi.")
        return 0
    else:
        return tagihan


menu = 0

while (menu != 5):
    print("============================")
    print("Program ATM")
    print("1. Cek Saldo")
    print("2. Tarik Saldo")
    print("3. Transfer")
    print("4. Bayar Listrik")
    print("5. Keluar program")
    print("============================")
    menu = int(input("Masukkan menu: "))

    if (menu == 1):
        cek()
    elif (menu == 2):
        jumlah_tarikan = tarik()
        if jumlah_tarikan != 0:
            isi_ATM -= jumlah_tarikan
            print("Penarikan berhasil! Saldo Anda sekarang:", jumlah_tarikan)
    elif (menu == 3):
        jumlah_transfer = transfer()
        if jumlah_transfer != 0:
            isi_ATM -= jumlah_transfer
            print('Berhasil transfer, saldo Anda sekarang', isi_ATM)
    elif (menu == 4):
        jumlah_tagihan = bayar_listrik_air()
        if jumlah_tagihan != 0:
            if jumlah_tagihan <= isi_ATM:
                isi_ATM -= jumlah_tagihan
                print("Pembayaran berhasil! Saldo Anda sekarang:", isi_ATM)
                print(identitas, air)
                print("Pembayaran ke")
                print(rekening_tujuan)
                print("Pembayaran telah selesai")
            else:
                print("Maaf, saldo tidak mencukupi.")
    elif (menu == 5):
        print("Anda telah keluar")
    else:
        print("Menu tidak valid, silakan pilih kembali.")
