
a = 20
b = 6

x = 15.5
y = 5.5

word1 = "///"
word2 = "|||"

full_string = word1 + " " + word2
print(full_string)

print(f"Додавання: {a} + {b} = {a + b}")
print(f"Віднімання: {x} - {y} = {x - y}")
print(f"Множення: {a} * {y} = {a * y}")
print(f"Ділення: {a} / {b} = {a / b}")  

full_string = word1 + " " + word2
print(full_string)


user_name = input("Як тебе звати? ")
age = int(input("Скільки тобі років? ")) # Конвертуємо в ціле число

print(f"Привіт, {user_name}! Через рік тобі буде {age + 1}.")