# Inisialisasi daftar kontak dalam bentuk dictionary
kontak = {}

# Fungsi untuk menambahkan kontak ke daftar
def tambah_kontak(nama, nomor):
    kontak[nama] = nomor
    print(f"Kontak '{nama}' dengan nomor '{nomor}' telah ditambahkan.")

# Fungsi untuk mencari kontak berdasarkan nama
def cari_kontak(nama):
    if nama in kontak:
        print(f"Nama: {nama}, Nomor: {kontak[nama]}")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk menghapus kontak dari daftar
def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak '{nama}' telah dihapus.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk menampilkan semua kontak
def tampilkan_kontak():
    if kontak:
        print("Daftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"Nama: {nama}, Nomor: {nomor}")
    else:
        print("Daftar kontak kosong.")

# Program utama
while True:
    print("\nPilihan:")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Hapus Kontak")
    print("4. Tampilkan Kontak")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '1':
        nama = input("Masukkan nama kontak: ")
        nomor = input("Masukkan nomor kontak: ")
        tambah_kontak(nama, nomor)
    elif pilihan == '2':
        nama = input("Masukkan nama kontak yang akan dicari: ")
        cari_kontak(nama)
    elif pilihan == '3':
        nama = input("Masukkan nama kontak yang akan dihapus: ")
        hapus_kontak(nama)
    elif pilihan == '4':
        tampilkan_kontak()
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
