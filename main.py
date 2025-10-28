class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.hungry = True

    def eat(self):
        print(f"{self.name} поїв і став ситим.")
        self.hungry = False
        self.energy += 20

    def sleep(self):
        print(f"{self.name} солодко спить...")
        self.energy += 30

    def play(self):
        print(f"{self.name} грається з клубком ниток!")
        self.energy -= 20
        self.hungry = True


# приклад використання
bonya = Cat("Боня")
bonya.play()
bonya.eat()
bonya.sleep()

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.knowledge = 50
        self.energy = 50
        self.day = 1

    def study(self):
        print(f"{self.name} вчиться ")
        self.knowledge += 10
        self.energy -= 10
        self.money -= 5

    def work(self):
        print(f"{self.name} працює ")
        self.money += 30
        self.energy -= 15

    def rest(self):
        print(f"{self.name} відпочиває ")
        self.energy += 20
        self.money -= 10

    def live_day(self):
        print(f"\nДень {self.day}:")
        print(f" Гроші: {self.money} |  Знання: {self.knowledge} | ⚡ Енергія: {self.energy}")

        actions = [self.study, self.work, self.rest]
        random.choice(actions)()  # випадковий вибір дії

        self.day += 1

    def live_year(self):
        for _ in range(12):  # умовно 12 днів = рік
            self.live_day()
        print(f"\n {self.name} прожив рік!")
        print(f" Гроші: {self.money}, Знання: {self.knowledge}, ⚡ Енергія: {self.energy}")


# створюємо студента
timofiy = Student("Тимофій")
timofiy.live_year()
