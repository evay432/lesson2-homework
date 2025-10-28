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
