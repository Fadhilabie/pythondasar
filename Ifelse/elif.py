# ELIF = else if statement
# nama = input("Nama kamu siapa? ")

# if nama == "ucup": # kondisi 1
# 	print("Hai ganteeeeng beuds!") # aksi true 1
# elif nama == "otong": # kondisi 2
# 	print("Hai si kece bangeeeets!!") # aksi true 2
# elif nama == "mario": # kondisi 3
# 	print("Hai humooooreeeesh!") # aksi true 3
# else:
# 	print("au ah gak kenal!!!") # aksi false
# print("sampai jumpa")

import math # Modul untuk perhitungan aritmatika
def kalkulator(): # Mengelompokan varibel
    angka1 = float(input("masukan angka 1 = ")) # Membuat variabel angka1 dengan metode input
    angka2 = float(input("masukan angka 2 = ")) # Membuat variabel angka2 dengan metode input
    oper = input("Masukan Operator(+,-,*,/,%) = ") # Membuat variabel operator untuk memasukan operator
    if oper == '+': # Operator penjumlahan
        hasil = angka1 + angka2
    elif oper == '-': # Operator pengurangan
        hasil = angka1 - angka2
    elif oper == '*': # Operator perkalian
        hasil = angka1 * angka2
    elif oper == '/': # Operator pembagian
        hasil = angka1 / angka2
    elif oper == '%': # Operator modulus
        hasil = angka1 % angka2
    hasil2 = int(hasil) # Membuat variable hasil2 untuk menampung output dari hasil
    print ("Jadi hasilnya adalah", hasil2) # Menampilkan operasi
kalkulator() # Menjalankan program def