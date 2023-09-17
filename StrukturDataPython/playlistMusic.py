# Program: Manajemen Playlist Musik dengan Tipe Data Tuple
# Karena Tuple tidak bisa diubah maka saya buat set

# Inisialisasi playlist musik kosong
playlist = set(["Sanes", "Rungkad", "Pingal"])

# Fungsi untuk menambahkan lagu ke playlist


def tambah_lagu(lagu):
    playlist.add(lagu)
    print(f"Lagu {lagu} Ditambahkan")

# Fungsi untuk menghapus lagu dari playlist


def hapus_lagu(lagu):
    if lagu in playlist:
        playlist.discard(lagu)
        print(f"Lagu {lagu} Dihapus")
    else:
        print(f"Lagu {lagu} Raono")

# Fungsi untuk menampilkan playlist


def tampilkan_playlist():
    if playlist:
        print("Daftar Lagu:")
        index = 1
        for lagu in playlist:
            print(f"{index}. {lagu}")
            index += 1
    else:
        print("Lagu Kosong.")


# Program utama
while True:
    # Gantilah opsi berikut dengan opsi yang sesuai
    print("\nSpotiify:")
    print("1. Tambah Lagu")
    print("2. Hapus Lagu")
    print("3. Lihat Playlist")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        lagu = input("Tambah lagu opo:")
        tambah_lagu(lagu)
    elif pilihan == '2':
        lagu = input("Hapus Lagu opo:")
        hapus_lagu(lagu)
    elif pilihan == '3':
        tampilkan_playlist()
    elif pilihan == '4':
        print(f"Minggato su")
        break
    else:
        print("Milih sek bener su")
