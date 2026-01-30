import math

G = 11.80

def calculate_flight():
    try:
    
        v0 = float(input("Введіть початкову швидкість (м/с): "))
        angle_deg = float(input("Введіть кут вильоту (у градусах): "))

    
        angle_rad = math.radians(angle_deg)

    
        v0x = v0 * math.cos(angle_rad)
        v0y = v0 * math.sin(angle_rad)

        
        t_total = (2 * v0y) / G
        max_dist = v0x * t_total
        max_height = (v0y**2) / (2 * G)

        print("-" * 30)
        print(f"Дальність польоту: {max_dist:.2f} м")
        print(f"Максимальна висота: {max_height:.2f} м")
        print(f"Загальний час у повітрі: {t_total:.2f} с")
        print("-" * 30)

        print("Висота снаряда по секундах:")
        current_t = 0
        while current_t <= t_total:
            h_t = v0y * current_t - (G * current_t**2) / 2
            h_t = max(0, h_t)
            
            print(f"Час {current_t:3} с | Висота: {h_t:6.2f} м")
            current_t += 1
            
        if (current_t - 1) < t_total:
             print(f"Час {t_total:6.2f} с | Висота:  0.00 м (Приземлення)")
    except ValueError:
        print("Помилка: введіть числові значення.")
if __name__ == "__main__":
    calculate_flight()