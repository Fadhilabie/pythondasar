# Program ini digunakan untuk mencari data dalam daftar
# Fungsi cari_data menerima daftar dan data yang ingin dicari sebagai input
def cari_data(daftar, data):
    if data in daftar:
        return True
    else:
        return False


# Gunakan fungsi cari_data untuk mencari data dalam daftar berikut
data_mahasiswa = ["Alice", "Bob", "Charlie", "David"]

# Panggil fungsi cari_data untuk mencari data_yang_dicari dalam data_mahasiswa
inputUser = input("Goleki: ")

# Memanggil fungsi cari_data dan mencetak hasilnya
if cari_data(data_mahasiswa, inputUser):
    print("Data ditemokne")
else:
    print("Data raono")
