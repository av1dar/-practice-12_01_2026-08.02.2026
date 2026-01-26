import os

filename = "Google DINOZAVR"
current_score = 1500
try:
    with open(filename, "r") as f:
        best_score = int(f.read())
        print(f"Попередній рекорд: {best_score}")
except FileNotFoundError:
    print("Файл рекорду не знайдено. Це перша гра!")
    best_score = 0
if current_score > best_score:
    print(f"Вітаємо! Ваш новий рекорд: {current_score}")
    with open(filename, "w") as f:
        f.write(str(current_score))
else:
    print(f"Ех, GG-wp. Ваш рахунок: {current_score}")

with open(filename, "r") as f:
    print(f"[Ваш останній рекорд]: {f.read()}")