identitas = ["No rekening 5200411249", "Nama : Panji"]
air = [int(input("masukkan no seri : ",))]
rekening_tujuan = ["No rek.", 9348578935, "Nama : Aldi", "Bank BRI"]

isi_ATM = 3500000


def cek():
    print("Saldo anda pada ATM adalah: ", isi_ATM)


def tarik():
    tarik_uang = isi_ATM - (int(input("masukkan jumlah penarikan : ")))
    return tarik_uang
    print(tarik())


def transfer():
    no_rek = int(input("masukkan nomor rekening : "))
    nama = str(input("masukkan nama penerima transfer tujuan : "))
    beri = int(input("Masukkan jumlah yang ingin di transfer : "))
    tf = isi_ATM - beri
    print(no_rek, nama, beri)
    print("--------------------------")
    print(identitas, "Rp.", tf)


def bayar_listrik_air():
    tag = 350000
    bayar = isi_ATM - tag
    print(bayar)
    print(identitas, air)
    print("Pembayaran ke")
    print(rekening_tujuan)
    print("Pembayaran telah selesai")


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
        tarik()
    elif (menu == 3):
        transfer()
    elif (menu == 4):
        bayar_listrik_air()
    else:
        print("Anda telah keluar")
