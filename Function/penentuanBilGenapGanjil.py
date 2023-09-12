# Program ini digunakan untuk menentukan apakah suatu bilangan adalah genap atau ganjil
# Fungsi cek_genap_ganjil menerima sebuah bilangan sebagai input dan mengembalikan hasil
def cek_genap_ganjil(bilangan):
    hasil = bilangan % 2
    return hasil


# Panggil fungsi cek_genap_ganjil untuk menentukan apakah bilangan adalah genap atau ganjil
bilanganmu = int(input("Lebokno angka: "))
cek = cek_genap_ganjil(bilanganmu)
if cek == 0:
    print("Bilanganmu genap")
else:
    print("Bilanganmu ganjil")
