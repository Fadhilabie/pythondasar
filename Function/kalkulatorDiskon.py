# Program ini digunakan untuk menghitung harga setelah diskon
# Fungsi hitung_diskon menerima harga awal dan persentase diskon sebagai input
def hitung_diskon(harga_awal, persentase_diskon):
    jumlah_diskon = (persentase_diskon / 100) * harga_awal
    hitung_diskon = harga_awal - jumlah_diskon
    return hitung_diskon


# Panggil fungsi hitung_diskon untuk menghitung harga setelah diskon
harga_awal = float(input("Lebokno rego: "))
persentase_diskon = float(input("Diskone pirang persen: "))
harga_diskon = hitung_diskon(harga_awal, persentase_diskon)

# Tampilkan harga setelah diskon
print(f"Harga sak wise diskon yaiku: {harga_diskon}k")
