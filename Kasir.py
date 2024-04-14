# ===================================================#
# Program Kasir untuk mencatat belanja pelanggan
# Versi Lengkap dengan Penjelasan dan Fitur Tambahan
# ===================================================#

# Import library
import os

# ---------------------------------------------------#
# Sub program (fungsi dan prosedur)
# ---------------------------------------------------#


def catat_transaksi():
    """Fungsi untuk mencatat transaksi belanja baru."""
    lagi = 'Y'
    barang = 0

    while lagi.upper() != 'T':
        # Bersihkan layar
        os.system('cls')

        # Menampilkan daftar barang
        tampil_daftar_barang(list_barang)

        # Meminta input kode dan jumlah barang yang dibeli
        kode = input("Input kode barang\t: ")
        jumlah = int(input("Jumlah barang\t\t: "))

        # Mencari data barang dari list_barang
        barang = cari_barang(list_barang, kode)

        # Jika barang tidak ditemukan, tampilkan pesan error
        if barang is None:
            print("Barang dengan kode", kode, "tidak ditemukan.")
            continue

        # Update total_harga
        total_harga = barang["jumlah_transaksi"] + jumlah

        # Tampilkan detail transaksi
        tampil_detail_transaksi(barang, jumlah, total_harga)

        # Update data 'jumlah_transaksi' dari barang tersebut
        barang["jumlah_transaksi"] = total_harga

        # Tanya user apakah mau input data transaksi lagi atau tidak
        lagi = input("Input data belanja lagi (Y/T)? ")


def tampil_daftar_barang(list_barang):
    """Fungsi untuk menampilkan daftar barang."""
    print("-" * 53)
    print("Kode".ljust(8), "Nama Barang".ljust(15),
          "Harga".ljust(11), "Jumlah Transaksi".ljust(18))
    print("-" * 53)

    for barang in list_barang:
        print(barang["kode"].ljust(8), barang["nama"].ljust(15), str(
            barang["harga"]).ljust(11), str(barang["jumlah_transaksi"]).ljust(18))

    print("-" * 53)


def cari_barang(list_barang, kode):
    """Fungsi untuk mencari barang berdasarkan kode."""
    for barang in list_barang:
        if barang["kode"] == kode.lower():
            return barang
    return None


def tampil_detail_transaksi(barang, jumlah, total_harga):
    """Fungsi untuk menampilkan detail transaksi."""
    print("-" * 53)
    print("Nama barang\t\t:", barang["nama"])
    print("Harga satuan\t\t: Rp", barang["harga"])
    print("---------------------------------")
    print("TOTAL TRANSAKSI\t: Rp", total_harga)
    print("---------------------------------")


def pilih_menu():
    """Fungsi untuk menampilkan menu dan mendapatkan input dari user."""
    # Tampilkan menu
    print("MENU PROGRAM:")
    print("1. Catat transaksi baru")
    print("2. Lihat laporan transaksi")
    print("3. Keluar")

    # Meminta input menu dari user
    pilih = int(input("Pilih menu: "))

    # Validasi input menu
    while pilih < 1 or pilih > 3:
        print("Menu yang dipilih tidak tersedia.")
        pilih = int(input("Pilih menu: "))

    return pilih


def tampil_laporan(list_barang):
    """Fungsi untuk menampilkan laporan transaksi."""
    # Cetak header tabel
    print("-" * 53)
    print("Kode".ljust(8), "Nama Barang".ljust(15),
          "Harga".ljust(11), "Jumlah Transaksi".ljust(18))
    print("-" * 53)

    # Tampilkan isi list_barang
    for barang in list_barang:
        print(barang["kode"].ljust(8), barang["nama"].ljust(15), str(
            barang["harga"]).ljust(11), str(barang["jumlah_transaksi"]).ljust(18))

    # Cetak garis bawah
    print("-" * 53)

# ---------------------------------------------------#
# Program utama
# ---------------------------------------------------#


# Variabel menu
menu = 0

# Menyiapkan list yang berisi dictionary untuk
# Menyiapkan list yang berisi dictionary untuk menyimpan data SEMUA barang
list_barang = [{"kode": 'p01', "nama": 'susu', 'harga': 3000, 'jumlah_transaksi': 0},
               {"kode": 'p02', "nama": 'roti', 'harga': 7000, 'jumlah_transaksi': 0},
               {"kode": 'p03', "nama": 'gula', 'harga': 9000, 'jumlah_transaksi': 0},
               {"kode": 'p04', "nama": 'kopi', 'harga': 5000, 'jumlah_transaksi': 0}]
while (menu != 3):
    # Bersihkan layar
    os.system('cls')

    # Pilih menu
    pilih = pilih_menu()

    # Cek menu
    if (pilih == 1):
        # Catat transaksi belanja
        catat_transaksi()

    elif (pilih == 2):
        # Tampilkan laporan transaksi belanja
        tampil_laporan(list_barang)

        # Berhenti hingga user menekan ENTER
        input("Tekan ENTER untuk melanjutkan ")

    elif (pilih == 3):
        # Menampilkan informasi bahwa user telah keluar dari program
        print("Anda telah keluar dari program.")

    else:
        # Menampilkan informasi bahwa menu yang diinputkan tidak tersedia
        print("Menu yang dipilih tidak tersedia.")
        # Berhenti hingga user menekan ENTER
        input("Tekan ENTER untuk melanjutkan ")
