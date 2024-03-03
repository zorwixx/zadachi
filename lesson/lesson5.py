class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} щось каже"


class Dog(Animal):
    def bark(self):
        return f"{self.name} голосно гавкає"


animal = Animal("Тварина")
print(animal.speak()) #Виведе: Тварина щомь каже

dog = Dog("Собака")
print(dog.speak()) #Виведе: Собака щось каже
print(dog.bark()) #Виведе: собака голосно гавкає

class BreedDog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} і {self.name} є {self.breed}"

breed_dog = BreedDog("Собака","Dog")
print(breed_dog.speak())

class Myclass:
    def __init__(self, value):
        self.__my_private_method(value)

    def __my_private_method(self, value):
        print(f"Private method called with value: {value}")

obj = Myclass(42)