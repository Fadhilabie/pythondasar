import math  # Modul untuk perhitungan aritmatika


def kalkulator():  # Mengelompokan varibel
    # Membuat variabel angka1 dengan metode input
    angka1 = float(input("masukan angka 1 = "))
    # Membuat variabel angka2 dengan metode input
    angka2 = float(input("masukan angka 2 = "))
    # Membuat variabel operator untuk memasukan operator
    oper = input("Masukan Operator(+,-,*,/,%) = ")
    if oper == '+':  # Operator penjumlahan
        hasil = angka1 + angka2
    elif oper == '-':  # Operator pengurangan
        hasil = angka1 - angka2
    elif oper == '*':  # Operator perkalian
        hasil = angka1 * angka2
    elif oper == '/':  # Operator pembagian
        hasil = angka1 / angka2
    elif oper == '%':  # Operator modulus
        hasil = angka1 % angka2
    # Membuat variable hasil2 untuk menampung output dari hasil
    hasil2 = int(hasil)
    print("Jadi hasilnya adalah", hasil2)  # Menampilkan operasi


kalkulator()  # Menjalankan program def
