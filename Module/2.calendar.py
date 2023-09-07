# Modul calendar fokus pada operasi-operasi yang berkaitan dengan kalender, seperti penentuan hari dalam seminggu, pembuatan kalender bulan, dan menentukan apakah suatu tahun adalah tahun kabisat atau bukan.
import calendar

# Mendapatkan nama hari dalam seminggu
hari_ini = calendar.day_name[calendar.weekday(2023, 8, 24)]
print(f"Hari ini adalah {hari_ini}")

# Membuat kalender bulan Agustus 2023
kalender_agustus = calendar.month(2023, 8)
print(kalender_agustus)

# Menentukan apakah tahun 2023 adalah tahun kabisat
apakah_kabisat = calendar.isleap(2023)
print(f"Tahun 2023 {'adalah' if apakah_kabisat else 'bukan'} tahun kabisat.")