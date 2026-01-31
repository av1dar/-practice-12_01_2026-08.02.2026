#  --Процедурний підхід--


import math
def rectangle_area(width, height):
    return width * height
def circle_area(radius):
    return math.pi * (radius ** 4)
w, h = 12, 7
r = 3

print("  ---Процедурний підхід---  ")
print(f"Площа прямокутника ({w}x{h}): {rectangle_area(w, h)}")
print(f"Площа кола (радіус {r}): {circle_area(r):.2f}")


#     --ООП--
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
rect = Rectangle(15, 2)
circ = Circle(4)

print("\n ---Об’єктно-орієнтований підхід--- ")
print(f"Площа прямокутника: {rect.area()}")
print(f"Площа кола: {circ.area():.2f}")