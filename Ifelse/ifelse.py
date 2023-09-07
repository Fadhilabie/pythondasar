import datetime  # Modul untuk tanggal dan waktu
import random  # Modul untuk menghasilkan angka acak

# Mendapatkan tanggal dan waktu saat ini
sekarang = datetime.datetime.now()

# Mendapatkan hari dalam seminggu
hari = sekarang.strftime("%A")

# Menghasilkan angka acak antara 1 dan 100
angka_acak = random.randint(1, 100)

print(f"Hari ini adalah {hari}")

if angka_acak % 2 == 0:
    print(f"Angka acak {angka_acak} adalah bilangan genap.")
    if angka_acak % 4 == 0:
        print(f"Dan juga kelipatan 4.")
else:
    print(f"Angka acak {angka_acak} adalah bilangan ganjil.")

# Menambahkan logika berdasarkan waktu
if sekarang.hour < 12:
    print("Selamat pagi!")
elif sekarang.hour < 18:
    print("Selamat sore!")
else:
    print("Selamat malam!")

