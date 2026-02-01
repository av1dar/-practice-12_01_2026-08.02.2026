class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Тиша...")
        
        
class Dog(Animal):
    def sound(self):
        print(f"Dog {self.name}: Гав-гав!")
class Cat(Animal):
    def sound(self):
        print(f"Cat {self.name}: Мяу!")
class Cow(Animal):
    def sound(self):
        print(f"Cow {self.name}: Му-у!")
zoo_animals = [
    Dog("рекс"),
    Cat("Мурчик"),
    Cow("Муся"),
    Dog("Патрон")
]

print("--- Початок циклу ---")
for animal in zoo_animals:
    animal.sound()