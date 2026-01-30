def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
try:
    user_input = input("Введіть числа через пробіл: ")
    numbers = [float(x) for x in user_input.split()]
    if not numbers:
        print("Список порожній.")
    else:
        print(f"Початковий масив: {numbers}")
        sorted_numbers = bubble_sort(numbers)
        print(f"Відсортований масив: {sorted_numbers}")
except ValueError:
    print("Похибка: будь ласка, вводьте числа через пробіл.")