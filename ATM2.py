import os


def clear():
    os.system("cls")


rekening = [{'norek': 111,
             'pin': 1234,
             'nama': 'Jeff',
             'saldo': 1000000,
             'bank': 'BCA'},
            {'norek': 112,
             'pin': 4321,
             'nama': 'Rafi',
             'saldo': 1500000,
             'bank': 'BCA'}]

air = [{'seri': 221,
        'nama': 'Ali',
        'tagihan': 170000},
       {'seri': 222,
        'nama': 'Sarif',
        'tagihan': 83000}]

listrik = [{'seri': 331,
           'nama': 'Kiki',
            'tagihan': 70000},
           {'seri': 332,
           'nama': 'Agung',
            'tagihan': 90000}]


def selesai():
    print('Program Telah Selesai')
    exit()


def ulang():
    print()
    pil = input('Kembali ke menu? y/n : ')

    if pil == 'y':
        menu()
    else:
        selesai()


def login(pin):
    for i in range(len(rekening)):
        if rekening[i]['pin'] == pin:
            return i


def cek_rek(no_rek):
    for i in rekening:
        if i['norek'] == no_rek:
            return i


def cek_air(no_seri):
    for i in air:
        if i['seri'] == no_seri:
            return i


def cek_lis(no_seri):
    for i in listrik:
        if i['seri'] == no_seri:
            return i


def transfer(i):
    saldo = rekening[i]['saldo']
    print("=================================")
    no_rek = int(input('Msukan No Rekening : '))
    nom = int(input('Msukan Nominal yg ditransfer : Rp.'))
    rekTujuan = cek_rek(no_rek)

    if rekTujuan == None:
        print('Maaf No Rekening Tidak Terdaftar')
        ulang()
    if nom > saldo:
        print('Maaf Saldo Anda Tidak Cukup')
        ulang()

    print("=================================")
    print("No Rek : ", no_rek)
    print("Nama : ", rekTujuan['nama'])
    print("Bank : ", rekTujuan['bank'])
    print()
    print("Nominal Transfer : Rp.", nom)

    pil = input('Lakukan Transaksi? y/n : ')
    if pil == 'y':
        rekTujuan['saldo'] = rekTujuan['saldo']+nom
        rekening[i]['saldo'] = saldo-nom
        print("Transaksi Berhasil")
        ulang()
    else:
        ulang()


def pem_air(i):
    saldo = rekening[i]['saldo']
    print("=================================")
    no_seri = int(input('Msukan No Seri: '))
    seri = cek_air(no_seri)

    if seri == None:
        print('Maaf No Seri Tidak Ditemukan')
        ulang()

    print("=================================")
    print("No Seri : ", no_seri)
    print("Nama : ", seri['nama'])
    print("Total Tagihan : ", seri['tagihan'])
    print()
    pil = input('Lakukan Pembayaran? y/n : ')
    if pil == 'y':
        rekening[i]['saldo'] = saldo-seri['tagihan']
        seri['tagihan'] = 0
        print("Pembayaran Berhasil")
        ulang()
    else:
        ulang()


def pem_listrik(i):
    saldo = rekening[i]['saldo']
    print("=================================")
    no_seri = int(input('Msukan No Seri: '))
    seri = cek_lis(no_seri)

    if seri == None:
        print('Maaf No Seri Tidak Ditemukan')
        ulang()

    print("=================================")
    print("No Seri : ", no_seri)
    print("Nama : ", seri['nama'])
    print("Total Tagihan : ", seri['tagihan'])
    print()
    pil = input('Lakukan Pembayaran? y/n : ')
    if pil == 'y':
        rekening[i]['saldo'] = saldo-seri['tagihan']
        seri['tagihan'] = 0
        print("Pembayaran Berhasil")
        ulang()
    else:
        ulang()


def menu():
    clear()
    pin = int(input('Masukan Pin : '))
    i = login(pin)

    if i == None:
        print("Maaf PIN Anda Salah ")
        ulang()
    saldo = rekening[i]['saldo']
    print("Halo kak ", rekening[i]['nama'])
    print("SELAMAT DATANG DI ATM BANK BCA")
    print("1.Cek Saldo")
    print("2.Tarik Tunai")
    print("3.Transfer")
    print("4.Pembayaran")
    print("5.Keluar ATM")

    pil = int(input('Masukan Menu Pilihan : '))

    if pil == 1:
        print()
        print("Saldo Anda Saat Ini : Rp. ", saldo)
        ulang()

    elif pil == 2:
        tarik = int(input('Masukan  yang ingin ditarik : '))
        if tarik > saldo:
            print("Saldo Anda Tidak Cukup ")
            ulang()
        else:
            saldo = rekening[i]['saldo']-tarik
            print("Penarikan Berhasil ")
            print("Saldo Saat ini : Rp. ", saldo)
            ulang()
    elif pil == 3:
        transfer(i)

    elif pil == 4:
        clear()
        print("Pilih Pembayaran")
        print("1.Listrik")
        print("2.Air")
        pill = int(input("Pilih : "))
        if pill == 1:
            pem_listrik(i)
        else:
            pem_air(i)

    else:
        selesai()


menu()
