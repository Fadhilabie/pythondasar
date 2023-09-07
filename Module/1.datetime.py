# Digunakan untuk bekerja dengan objek-objek yang berkaitan dengan tanggal dan waktu. Termasuk pengaturan dan pengambilan tanggal dan waktu saat ini, perhitungan selisih waktu, pemformatan tanggal, dan banyak lagi.
import datetime

sekarang = datetime.datetime.now()
print(sekarang)

tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day
jam = sekarang.hour
menit = sekarang.minute
detik = sekarang.second

print(f"Tanggal: {tahun}-{bulan}-{hari}")