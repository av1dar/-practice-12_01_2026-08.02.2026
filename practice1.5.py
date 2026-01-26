

print("--- 1. Робота з Рядками (Immutability) ---")
card_number = "1234-5678-9876-5432"
last_four = card_number[-4:] 
print(f"Останні цифри: {last_four}")
masked_card = ("X" * 15) + last_four
print(f"Оригінал: {card_number}")
print(f"Маска:    {masked_card}")




print("\n--- 2. Робота зі Списками (Mutability) ---")
cart = ["Хліб", "Молоко", "Яйця", "Масло", "Сир"]
print(f"Перші покупки: {cart[:2]}")
print(f"Кожен другий товар: {cart[::2]}")
print(f"До зміни: {cart}")
cart[1] = "Кефір"  
print(f"Після зміни: {cart}")
reversed_cart = cart[::-1]
print(f"Зворотний порядок: {reversed_cart}")