def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
try:
    num = int(input("Введіть ціле невід'ємне число: "))
    if num < 0:
        print("Похибка: факторіал визначений тільки для невід'ємних чисел.")
    elif num > 900: 
        print("Число занадто велике для стандартної рекурсії.")
    else:
        result = factorial_recursive(num)
        print(f"Факторіал {num}! = {result}")
except ValueError:
    print("Похибка: введіть ціле число.")