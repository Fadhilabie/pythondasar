# Fungsi pembagian_bulat menerima dua angka sebagai input dan mengembalikan hasil pembagian bulat
def pembagian_bulat(angka1, angka2):
    hasil_pembagian = round(angka1 / angka2)
    return hasil_pembagian


# Gunakan fungsi pembagian_bulat untuk menghitung pembagian bulat dari dua angka berikut
angka1 = int(input("Lebokne angka: "))
angka2 = int(input("Meneh: "))

# Panggil fungsi pembagian_bulat untuk menghitung hasil pembagian bulat
hasil_pembagian_bulat = pembagian_bulat(angka1, angka2)

# Tampilkan hasil pembagian bulat
print("Hasil pembagian bunder:", hasil_pembagian_bulat)
