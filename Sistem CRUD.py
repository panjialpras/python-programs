import os

# sub program


def tambah_data_mhs():
    input_nim = input("NIM\t\t: ")
    input_nama = input("Nama Lengkap\t: ")
    input_gender = input("Gender (L/P)\t: ")
    input_prodi = input("Program Studi\t: ")
    input_ipk = float(input("IPK\t\t: "))

    # mengisi data ke dictionary
    data_mhs = {"nim": input_nim,
                "nama": input_nama,
                "gender": input_gender,
                "prodi": input_prodi,
                "ipk": input_ipk}

    # memasukkan data dictionary ke dalam list
    data_semua_mhs.append(data_mhs)


def tampil_data_mhs():
    if (len(data_semua_mhs) == 0):
        print("Data mahasiswa masih kosong")
    else:
        print("-" * 64)
        print("NIM".ljust(5), "Nama Mahasiswa".ljust(20),
              "Gender".ljust(8),  "Program Studi".ljust(20), "IPK")
        print("-" * 64)

        # menampilkan satu per satu dictionary data_mhs di dalam list data_semua_mhs
        for mhs in data_semua_mhs:
            print(mhs["nim"].ljust(5), mhs["nama"].ljust(
                20), mhs["gender"].ljust(8), mhs["prodi"].ljust(20), mhs["ipk"])


def hapus_data_mhs(nim):

    ketemu = 0  # penanda apakah data itu ada atau tidak
    for mhs in data_semua_mhs:
        if (mhs["nim"] == nim):
            # update ketemu
            ketemu = 1

            # hapus data
            # data_semua_mhs.pop(idx)
            data_semua_mhs.remove(mhs)
            print("Data yang dicari telah dihapus!")

            # hentikan pencarian
            break

    # tampilkan hasil jika data tidak ditemukan
    if (ketemu == 0):
        print("Data yang dicari tidak ditemukan!")


def cari_data_mhs(nim):

    ketemu = 0
    for mhs in data_semua_mhs:
        if (mhs["nim"] == nim):
            # update ketemu
            ketemu = 1

            # cetak data
            print("Data ditemukan!")
            print("---------------------------------")
            print("NIM          :", mhs["nim"])
            print("Nama Lengkap :", mhs["nama"])
            print("Gender       :", mhs["gender"])
            print("Program Studi:", mhs["prodi"])
            print("IPK          :", mhs["ipk"])

            # hentikan pencarian
            break

    # tampilkan info jika data tidak ditemukan
    if (ketemu == 0):
        print("Data yang dicari tidak ditemukan!")

    '''i = 0
    while (i < len(data_semua_mhs) and ketemu == 0):
        if (nim == data_semua_mhs[i]["nim"]):
            ketemu = 1

            #cetak data
            print("Data ditemukan!")
            print("---------------------------------")
            print("NIM          :", data_semua_mhs[i]["nim"])
            print("Nama Lengkap :", data_semua_mhs[i]["nama"])
            print("Gender       :", data_semua_mhs[i]["gender"])
            print("Program Studi:", data_semua_mhs[i]["prodi"])
            print("IPK          :", data_semua_mhs[i]["ipk"])'''


# program utama
# inisialisasi variabel global (variabel yang bisa diakses lewat manapun)
data_mhs = {}  # dictionary
data_semua_mhs = []  # list
menu = 0  # variabel biasa

while (menu != 5):
    # membersihkan layar command prompt
    os.system("cls")

    # menampilkan menu
    print("----------------------------")
    print("Aplikasi Pendataan Mahasiswa UTY")
    print("1. Lihat Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Cari Data Mahasiswa")
    print("5. Keluar")
    print("----------------------------")
    menu = int(input("Pilih Menu: "))

    # cek menu
    if (menu == 1):
        tampil_data_mhs()
    elif (menu == 2):
        tambah_data_mhs()
    elif (menu == 3):
        hapus = input("Masukkan NIM yang akan dihapus: ")
        hapus_data_mhs(hapus)
    elif (menu == 4):
        cari = input("Masukkan NIM yang ingin dicari: ")
        cari_data_mhs(cari)
    elif (menu == 5):
        print("Anda telah keluar")
    else:
        print("Menu yang dipilih tidak tersedia")

    # menunggu user menekan enter untuk melanjutkan
    input("\nTekan ENTER untuk melanjutkan")
