import datetime

sekarang = datetime.datetime.now()

tahun_lahir = int(input("Tahun Kelahiran Anda: "))
bulan_lahir = int(input("Bulan Kelahiran Anda: "))
tanggal_lahir = int(input("Tanggal Kelahiran Anda: "))
# Hitung umur


def umur():
    lahir_tanggal = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
    selisih = sekarang - lahir_tanggal
    tahun = selisih.days // 365
    sisa_hari = selisih.days % 365
    bulan = sisa_hari // 30
    hari = sisa_hari % 30
    return tahun, bulan, hari


usia_tahun, usia_bulan, usia_hari = umur()
print(
    f"Anda berusia {usia_tahun} tahun, {usia_bulan} bulan, dan {usia_hari} hari.")
# Menanyakan SIM
if usia_tahun >= 17:
    print(f"Anda berusia {usia_tahun} tahun. Anda layak mengendarai mobil.")
    jawaban = input("Sudah punya SIM belum? (y/n): ").lower()
    if jawaban == "y":
        print("Selamat! ayo join ngabers?")
    elif jawaban == "n":
        print("SIM gari nembak opo susahe to mbok gek di urus.")
    else:
        print("Jawab dengan 'y' atau 'n'.")
else:
    print("Anda belum layak mengendarai mobil karena usia Anda belum mencapai 17 tahun.")
