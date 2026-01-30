import math

print("Калькулятор для розв'язання квадратного рівнян1ня ax^2 + bx + c = 0")

try:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    if a == 0:
        print("Це не є квадратним рівнянням (a не може бути 0).")
    else:
        D = b**2 - 4*a*c
        print(f"Дискримінант D = {D}")
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print(f"Рівняння має два корені: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
        elif D == 0:
            x = -b / (2*a)
            print(f"Рівняння має один корінь: x = {round(x, 2)}")
        else:
            print("Рівняння не має дійсних коренів.")
except ValueError:
    print("Похибка: будь ласка, вводьте числові значення.")