class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def live_day(self):
        if self.energy < 30:
            self.energy += 50
            print(f"{self.name} спит. Энергия: {self.energy}%.")
        else:
            self.energy -= 20
            print(f"{self.name} играет. Энергия: {self.energy}%.")

cat = Cat("Мурзик")
for _ in range(5):
    cat.live_day()


class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.energy = 50

    def live_day(self):
        if self.money < 20:
            self.money += 50
            self.energy -= 10
            print(f"{self.name} работает. Деньги: {self.money}, Энергия: {self.energy}.")
        elif self.energy < 30:
            self.energy += 30
            self.money -= 10
            print(f"{self.name} отдыхает. Энергия: {self.energy}, Деньги: {self.money}.")
        else:
            self.energy -= 20
            print(f"{self.name} учится. Энергия: {self.energy}, Деньги: {self.money}.")

student = Student("Иван")
for _ in range(5):
    student.live_day()
