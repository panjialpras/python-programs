import os

#Fungsi untuk menghaspus tiap output jika sudah ada input agar bersih dan mudah untuk dibaca
def clear():
    os.system("cls")

#Fungsi untuk menyimpan data-data yang dibutuhkan
def tambah():
    input_nama = input("Nama\t\t: ")
    input_lama = int(input("Lama sewa\t: "))
    input_tgl = int(input("Tanggal\t: "))
    input_jam = int(input("Jam mulai\t: "))
    input_mnt = int(input("Menit ke?\t: "))
    tgl_selesai = "Tanggal selesai"

    # x = datetime.datetime.now (2021, 1, input_tgl)
    Jam_Selesai = input_jam + input_lama
    if int(Jam_Selesai) >= 24:
        Jam_Selesai = int(Jam_Selesai) - 24
        input_selesai = input_tgl + 1
    #Memasukkan data-data yang di inputkan ke dalam SET/array {} berupa key dan value
    isi = {"Nama": input_nama,
           "Lama sewa": input_lama,
           "Tanggal sewa": input_tgl,
           "Jam Mulai": input_jam,
           "Menit Mulai": input_mnt,
           "Jam_Selesai": Jam_Selesai,
           "Tanggal selesai": tgl_selesai}
    sama = 0

    for a in data_booking:

        if (input_tgl, input_jam, input_mnt) == (a["Tanggal sewa"], a["Jam Mulai"], a["Menit Mulai"]):
            sama = 1

    if sama == 1:
        print("data sudah ada")
    elif sama == 0:
        data_booking.append(isi)


def lihat_bookingan():
    if (len(data_booking) == 0):
        print("Data masih kosong")
    else:
        print("-" * 30)
        print("Nama", "Lama ", "Tanggal ", "Jam ",
              "Menit ", "Selesai", "Harga")
        print("-" * 30)

        for data in data_booking:
            print(data["Nama"], str(data["Lama sewa"]), str(data["Tanggal sewa"]), str(data["Jam Mulai"]), str(
                data["Menit Mulai"]), str(data["Jam_Selesai"]), 4000 * float(data["Jam Mulai"]))


def hapus_booking(nama):

    ada = 0
    for data in data_booking:
        if (data["Nama"] == nama):

            ada = 1
            data_booking.remove(data)
            print("Data telah dihapus")

            break

    if (ada == 0):
        print("Data tidak ada")


isi = {}
data_booking = []
menu = 0

while (menu != 4):

    clear()

    print("-----------------------")
    print("1. Tambah Booking")
    print("2. Cek Booking")
    print("3. Hapus Booking")
    print("4. Keluar")
    print("------------------------")

    menu = int(input("Pilih menu: "))

    if (menu == 1):
        tambah()
    elif (menu == 2):
        lihat_bookingan()
    elif (menu == 3):
        nama = input("Masukkan Nama yang ingin dihapus: ")
        hapus_booking(nama)
    else:
        print("Anda telah keluar")
    input("\nTekan ENTER untuk melanjutkan")
