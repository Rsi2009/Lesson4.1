class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 1

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость: {self.endurance}")

war1 = Warrior("Степа", 76, 54, "черный")
war2 = Warrior("Вася", 45, 76, "белый")

print(war1.endurance)
war1.sleep()
print(war1.endurance)

print(war1.power)
war1.eat()
print(war1.power)

war1.info()
war2.info()

