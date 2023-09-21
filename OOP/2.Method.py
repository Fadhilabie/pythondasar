class Hero:
    # Class Variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # Void function, method tanpa return
    def siapa(self):
        print("Namaku adalah " + self.name)

    # Method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero('masha', 100, 10, 1)
hero2 = Hero('claude', 10, 10, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
