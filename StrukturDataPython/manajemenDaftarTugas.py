# Program: Manajemen List Daftar Tugas

# Inisialisasi daftar tugas
tugas = ["MTK", "BINDO", "PPKN"]

# Fungsi untuk menambahkan tugas ke daftar


def tambah_tugas(task):
    tugas.append(task)
    print(f"{task} Wes Ditambahne.")

# Fungsi untuk menghapus tugas dari daftar


def hapus_tugas(task):
    if task in tugas:
        tugas.remove(task)
        print(f"{task} Wes Dihapus.")
    else:
        print(f"Tugase Raono.")

# Fungsi untuk menampilkan semua tugas


def tampilkan_tugas():
    if tugas:
        print("Daftar Tugas:")
        nomor = 1
        for task in tugas:
            print(f"{nomor}. {task}")
            nomor += 1
    else:
        print("Daftar Kosong.")


# Program utama
while True:
    # Gantilah opsi berikut dengan opsi yang sesuai
    print("\nMeh Ngopo?:")
    print("1. Nambah Tugas")
    print("2. Mbusak Tugas")
    print("3. Ndelok Tugas")
    print("4. Minggat")

    pilihan = input("Lebokno (1/2/3/4): ")

    if pilihan == '1':
        task = input("Lebokne Tugas Anyare: ")
        tambah_tugas(task)
    elif pilihan == '2':
        task = input("Lebokne Tugas Sek Arep Dihapus:")
        hapus_tugas(task)
    elif pilihan == '3':
        tampilkan_tugas()
    elif pilihan == '4':
        print(f"Minggato cok")
        break
    else:
        print(f"pilihanmu Raceto")
