# Program ini digunakan untuk menentukan angka terbesar dari dua angka

# Fungsi angka_terbesar menerima dua angka sebagai input dan mengembalikan angka terbesar
def angka_terbesar(angka1, angka2):
    if angka1 > angka2:
        return angka1
    else:
        return angka2

# Mengambil input dari pengguna
input1 = int(input("Lebokne angka: "))
input2 = int(input("Meneh: "))

# Panggil fungsi angka_terbesar untuk menentukan angka terbesar
guedhe = angka_terbesar(input1, input2)

# Tampilkan angka terbesar
print("Angka sing paling guedi:", guedhe)