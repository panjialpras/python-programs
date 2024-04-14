todo = []

def TambahKegiatan():
    tambah = str(input("masukan aktivitas ke-{} :".format(len(todo)+1)))
    todo.append(tambah)
def HapusKegiatan():
    hapus = int(input("pilih nomor kegiatan yang ingin dihapus: "))
    todo.pop(hapus - 1)
def DaftarKegiatan():
    print("========== To Do List ==========")
    if(len(todo) == 0):
        print("Belum ada kegiatan")
    else:
        for i in range(len(todo)):
                print(str(i+1)+".", todo[i])
    print("========== To Do List ==========")


tampilan = "ya"
while(tampilan == "ya"):
    DaftarKegiatan()
    print("\n1.Tambah\n2.Hapus\n3.Keluar")

    pilih = int(input("Masukan pilihan: "))
    if(pilih == 1):
        ulang = "y"
        while(ulang == "y"):
            TambahKegiatan()
            ulang = str(input("tambah kegiatan lagi? y/t: "))
    elif(pilih == 2):
        if(len(todo) == 0):
            print("aktivitas masih kosong!")
            input("Tekan ENTER untuk melanjutkan...")
        else:
            ulang = "y"
            while(ulang == "y"):
                HapusKegiatan()
                print()
                DaftarKegiatan()
                ulang = str(input("hapus kegiatan lagi? y/t: "))
    else:
        tampilan = "tidak"
print("program selesai")