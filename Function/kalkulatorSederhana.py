# Program ini adalah kalkulator sederhana
# Fungsi penjumlahan menerima dua angka sebagai input dan mengembalikan hasil penjumlahan
def penjumlahan(angka1, angka2):
    hasil = angka1 + angka2
    print(hasil)

# Fungsi pengurangan menerima dua angka sebagai input dan mengembalikan hasil pengurangan

def pengurangan(angka1, angka2):
    hasil = angka1 - angka2
    print(hasil)

# Fungsi perkalian menerima dua angka sebagai input dan mengembalikan hasil perkalian
def perkalian(angka1, angka2):
    hasil = angka1 * angka2
    print(hasil)
    
# Fungsi pembagian menerima dua angka sebagai input dan mengembalikan hasil pembagian
def pembagian(angka1, angka2):
    hasil = angka1 / angka2
    print(hasil)

inputUser = input("Masukkan Opsi Operation: ")
inputAngka1 = int(input("Masukkan Parameter 1: "))
inputAngka2 = int(input("Masukkan Parameter2: "))

if inputUser == "+":
    penjumlahan(inputAngka1, inputAngka2)
elif inputUser == "-":
    pengurangan(inputAngka1, inputAngka2)
elif inputUser == "*":
    perkalian(inputAngka1, inputAngka2)
elif inputUser == "/":
    pembagian(inputAngka1, inputAngka2)