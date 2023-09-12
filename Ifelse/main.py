angka = input("Coba Masukkan Angka : ")

try:
    angka = int(angka)
    if angka == 0:
        print("Wow Nol Seperti Akhlaqmu!")
    elif angka > 0:
        print("Wow Positif")
    elif angka < 0:
        print("Wow Negatif Seperti Akhlaqmu!")
    else:
        print("GAK BERES LU")
except ValueError:
    print("GW KAN SURUH LU MASUKKAN ANGKA BUKAN HURUF")
