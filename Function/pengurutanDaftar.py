# Program ini digunakan untuk mengurutkan sebuah daftar angka
# Fungsi urutkan_daftar menerima sebuah daftar angka sebagai input dan mengembalikan daftar yang sudah diurutkan
def urutkan_daftar(daftar):
    daftar_urut = sorted(daftar)
    return daftar_urut

# Gunakan fungsi urutkan_daftar untuk mengurutkan daftar berikut
daftar_angka = [4, 2, 7, 1, 9]    

# Panggil fungsi urutkan_daftar untuk mengurutkan daftar_angka
daftar_urut = urutkan_daftar(daftar_angka)

# Tampilkan daftar yang sudah diurutkan
print("Daftar sek wes urut:", daftar_urut)