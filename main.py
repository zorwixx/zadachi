class Human:
    def __init__(self, name: str = "Sim", age: int = 0, energy: int = 100, happiness: int = 100, hunger: int = 0):
        """Конструктор класу Human."""
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger

    def eat(self, food: int):
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.name} ate. Hunger: {self.hunger}")


    def sleep(self, hours: int):
            self.energy += hours
            if self.energy > 100:
                self.energy = 100
            print(f"{self.name} slept. energy: {self.energy}")

    def play(self, activity: int):
        self.happiness += activity
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} played. happiness: {self.happiness}")


    def age_up(self, years: int = 1):
        self.age += years
        print(f"{self.name} aged up. Age: {self.age}")

    def status(self):
        print(f"{self.name}'s status - Age: {self.age}, energy: {self.energy}, happiness: {self.happiness}, Hunger: {self.hunger}")


sim1 = Human("Sim1")
sim1.eat(30)
sim1.sleep(8)
sim1.play(20)
sim1.age_up(5)

sim1.status()

