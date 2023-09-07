# Program ini digunakan untuk menghitung Indeks Massa Tubuh (BMI)
# Fungsi hitung_bmi menerima berat (dalam kilogram) dan tinggi (dalam meter) sebagai input
def hitung_bmi(berat, tinggi):
    hasil = berat / (tinggi * tinggi)
    return hasil

# Panggil fungsi hitung_bmi untuk menghitung BMI
beratmu = float(input("Beratmu Pirang Kilo: "))
tinggimu = float(input("Tinggimu Pirang Meter: "))
bmi = hitung_bmi(beratmu, tinggimu)

# Menentukan kategori berdasarkan nilai BMI
if bmi < 18.5:
    print("Kuru")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Diet")
else:   
    print("Kelemon")