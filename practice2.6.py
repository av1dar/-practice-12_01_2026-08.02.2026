class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} видає якийсь звук...")


class Dog(Animal):
    def sound(self):
        print(f"Dog {self.name} робить: Гав-гав!")
class Cat(Animal):
    def sound(self):
        print(f"Cat {self.name} робить: Мяу-мяу!")
class Cow(Animal):
    def sound(self):
        print(f"Cow {self.name} робить: Му-у-у!")

zoo = [
    Dog("Рекс"),
    Cat("Мурчик"),
    Cow("муся"),
    Animal("Невідома істота")
]
print("--- Концерт у зоопарку ---")
for animal in zoo:
    animal.sound()