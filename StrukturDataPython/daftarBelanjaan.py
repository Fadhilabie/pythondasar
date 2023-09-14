# Program: Manajemen Daftar Belanjaan dengan Struktur Data Set

# Inisialisasi daftar belanjaan dalam bentuk set
belanjaan = set(["MTK","BINDO","AGAMA"])

# Fungsi untuk menambahkan item ke daftar belanjaan


def tambah_item(item):
    belanjaan.add(item)
    print(f"{task} Item Bertambah")

# Fungsi untuk menghapus item dari daftar belanjaan


def hapus_item(item):
    if item in belanjaan:
        belanjaan.discard(item)
        print(f"{item} Item Dihapus")
    else:
        print(f"{item} Gak ono cok")

# Fungsi untuk menampilkan daftar belanjaan


def tampilkan_daftar():
    if belanjaan:
        print("Daftar Tugas:")
        nomor = 1
        for item in belanjaan:
            print(f"{nomor}. {item}")
            nomor += 1
    else:
        print("Daftar Kosong.")


# Program utama
while True:
    # Gantilah opsi berikut dengan opsi yang sesuai
    print("\nPilihan:")
    print("1. Tambah")
    print("2. Hapus")
    print("3. Ndelok")
    print("4. Minggat")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        task = input("Lebokne Tugas Anyare: ")
        tambah_item(task)
    elif pilihan == '2':
        task = input("Lebokne Tugas Sek Arep Dihapus:")
        hapus_item(task)
    elif pilihan == '3':
        tampilkan_daftar()
    elif pilihan == '4':
        print(f"Minggato cok")
        break
    else:
        print(f"pilihanmu Raceto")
