class Car:
    def __init__(self, brand, year, mileage):
        "Конструктор: ініціалізує атрибути при створенні об'єкта"
        self.brand = brand      
        self.year = year        
        self.mileage = mileage  

    def drive(self, km):
        "Метод для збільшення пробігу"
        if km > 0:
            self.mileage += km
            print(f"Рушаймо! Пробіг збільшено на {km} км.")
        else:
            print("Похибка: Кількість кілометрів має бути додатною.")

    def info(self):
        "Метод для виведення детальної інформації"
        print(f"--- Інфо авто ---")
        print(f"Марка: {self.brand}")
        print(f"Рік: {self.year}")
        print(f"Поточний пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.brand} ({self.year}) - {self.mileage} км"

my_car = Car("Toyota mark II", 2004, 23000)
my_car.info()
my_car.drive(235)
print(f"\nКороткий опис (через __str__): {my_car}")
my_car.info()