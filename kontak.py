import os


def tambah_kontak():
    nama = input("Nama: ")
    nomor_telp = int(input("Nomor Telepon: "))

    data_kontak = {
        "nama": nama,
        "nomor telepon": nomor_telp
    }

    tambah_data.append(data_kontak)


def tampil_data_kontak():
    if len(tambah_data) == 0:
        print("Data kontak kosong")
    else:
        print("-" * 32)
        print("Nama".ljust(20), "Nomor Telepon".ljust(12))

        for data in tambah_data:
            print(data["nama"].ljust(20), str(data["nomor telepon"]).ljust(12))


def hapus_kontak(nomor_telepon):
    ketemu = False

    for data in tambah_data:
        if data['nomor telepon'] == nomor_telepon:
            ketemu = True
            tambah_data.remove(data)
            print('Data yang dicari telah dihapus')
            break

    if not ketemu:
        print("Data yang dicari tidak ada")


tambah_data = []
menu = 0

while menu != 4:
    os.system("cls")

    print("---------------------")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Lihat Kontak")
    print("4. Keluar")
    print("---------------------")
    menu = int(input("Pilih Menu: "))

    if menu == 1:
        tambah_kontak()
    elif menu == 2:
        nomor_telepon = int(input("Masukkan nomor yang akan dihapus: "))
        hapus_kontak(nomor_telepon)
        input("\nTekan ENTER untuk kembali ke menu...")
    elif menu == 3:
        tampil_data_kontak()
        input("\nTekan ENTER untuk kembali ke menu...")
    elif menu == 4:
        print('Anda Telah Keluar Dari Sistem')
    else:
        print("Menu tidak ada")
        input("\nTekan ENTER untuk kembali ke menu...")
