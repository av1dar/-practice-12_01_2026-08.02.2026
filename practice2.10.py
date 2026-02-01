class Car:
    def __init__(self, model, mileage):
        self.model = model
        self._mileage = mileage 

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, new_value):
        if new_value < 0:
            print("Похибка: Пробіг не може бути від'ємним.")
        elif new_value < self._mileage:
            print(f"Халепа: Не можна зменшити пробіг! (Було: {self._mileage}, спроба: {new_value})")
        else:
            print(f"Пробіг оновлено: {self._mileage} -> {new_value}")
            self._mileage = new_value
my_car = Car("toyota chaser", 10000)
print(f"\nАвто: {my_car.model}, Пробіг: {my_car.mileage}")
my_car.mileage = 10500 
my_car.mileage = 5000  
print(f"Фінальний пробіг: {my_car.mileage}")