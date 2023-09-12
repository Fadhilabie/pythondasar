# Program ini digunakan untuk menentukan apakah sebuah kata adalah palindrom
kata = input("Kei aku kata kata boss: ")

# Fungsi cek_palindrom menerima sebuah kata sebagai input dan mengembalikan hasil


def cek_palindrom(kata):
    if kata == kata[::-1]:
        print("anjay kata katamu palindrom")
    else:
        print("b aja, kata katamu ra palindrom")


# Panggil fungsi cek_palindrom untuk menentukan apakah kata adalah palindrom
cek_palindrom(kata)
