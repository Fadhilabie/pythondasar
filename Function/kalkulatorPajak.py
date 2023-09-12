# Program ini digunakan untuk menghitung jumlah pajak yang harus dibayar
#  Fungsi hitung_pajak menerima penghasilan sebagai input dan mengembalikan jumlah pajak
def hitung_pajak(penghasilan):
    pajak = 0.05 * penghasilan
    return pajak


# Panggil fungsi hitung_pajak untuk menghitung jumlah pajak yang harus dibayar
inputGaji = float(input('Lebokno gajimu: '))
jumlah_pajak = hitung_pajak(inputGaji)

# Hitung penghasilan bersih
penghasilan_bersih = inputGaji - jumlah_pajak

# Tampilkan jumlah pajak dan penghasilan bersih
print(f'Bayaro pajak {jumlah_pajak}k')
print(f'Gaji resikmu {penghasilan_bersih}k')
