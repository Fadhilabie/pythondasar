jumlah_hari = int(
    input("Masukkan jumlah hari yang ingin dihitung pengeluarannya: "))
pengeluaran_harian = []
for hari in range(1, jumlah_hari + 1):
    pengeluaran = float(input(f"Masukkan pengeluaran untuk Hari ke-{hari}: "))
    pengeluaran_harian.append(pengeluaran)
total_pengeluaran = sum(pengeluaran_harian)
rata_rata_pengeluaran = total_pengeluaran / jumlah_hari
print(f"Total Pengeluaran Selama {jumlah_hari} Hari: {total_pengeluaran}")
print(f"Rata-rata Pengeluaran Harian: {rata_rata_pengeluaran}")
