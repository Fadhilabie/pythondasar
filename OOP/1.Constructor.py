class Hero:
    # Class variabel
    jumlah = 0
    # __init__ adalah metode untuk menginialisasi (mengatur nilai awal) atribut-atribut objek saat objek dari sebuah kelas dibuat
    # Self adalah parameter / cara objek berkomunikasi dengan dirinya sendiri.

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance variabel
        # Class name,health,power,armor adalah atribut
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama " + inputName)


hero1 = Hero("masha", 1000, 100, 4)
print(Hero.jumlah)
hero2 = Hero("claude", 100, 250, 1)
print(Hero.jumlah)
hero3 = Hero("miya", 100, 400, 0)
print(Hero.jumlah)
# Ketika baris kode di atas dieksekusi, Python akan membuat objek hero1,2,3 dari kelas Hero dan akan memanggil metode __init__ dengan argumen yang sesuai.
