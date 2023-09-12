nama = input("Masukkan Nama : ")
a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))
d = int(input("Masukkan Nilai D : "))
e = int(input("Masukkan Nilai E : "))

ratarata = (a + b + c + d + e) / 5
if ratarata >= 90 and ratarata <= 100:
    grade = "A"
    status = "Lulus"
elif ratarata >= 80:
    grade = "B"
    status = "Lulus"
elif ratarata >= 70:
    grade = "C"
    status = "Lulus"
elif ratarata >= 60:
    grade = "D"
    status = "Tidak Lulus"
else:
    grade = "E"
    status = "Tidak Lulus"

print(f"Nama : {nama}")
print(f"Mapel A : {a}")
print(f"Mapel B : {b}")
print(f"Mapel C : {c}")
print(f"Mapel D : {d}")
print(f"Mapel E : {e}")
print(f"Rata-rata : {ratarata}")
print(f"Grade : {grade}")
print(status)
