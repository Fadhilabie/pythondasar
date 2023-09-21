class Hero:  # Template
    # Class Variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variabel
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
