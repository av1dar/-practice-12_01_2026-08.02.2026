

print("--- Фейс-контроль 'бавона клуб' ---")


age = int(input("Ваш вік: "))
has_vip_card = input("Маєте VIP карту?: ")
is_drunk = input("Ви тверезі?: ")


if is_drunk == "ні": 
    print("Ви п'яні. Вхід заборонено одразу.")
else:
    if age >= 21:
        print("Проходьте, гарного вечора.")
        if has_vip_card == "так":
            print("Адміністратор проведе вас у VIP-ложу.")
    elif age >= 18 and has_vip_card == "так": 
        print("Вам ще немає 21, але як виняток для VIP - проходьте.")
    else:
        years_to_wait = 21 - age
        print(f"Вибачте, вхід тільки для дорослих. Приходьте через {years_to_wait} років.")
print("--- Наступний! ---")