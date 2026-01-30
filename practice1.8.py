import pandas as pd
import os

FILENAME = 'students_data.csv'

def handle_students_pandas():

    if not os.path.exists(FILENAME):
        data = {
            "Прізвище": ["Шевченко", "Кізяков", "Коляденко"],
            "Ім'я": ["Тарас", "Іван", "Дмитро"],
            "Математика": [80, 85, 67],
            "Фізика": [67, 70, 90],
            "Історія": [90, 74, 94],
            "Програмування": [92, 86, 75],
            "Англійська": [72, 82, 80]
        }
        df = pd.DataFrame(data)
        df.to_csv(FILENAME, index=False, encoding='utf-8-sig')
        print(f"Файл {FILENAME} створено.")
    else:
        df = pd.read_csv(FILENAME)
        print(f"Дані завантажено з файлу {FILENAME}.")

    subjects = ["Математика", "Фізика", "Історія", "Програмування", "Англійська"]

    df['Середній бал студента'] = df[subjects].mean(axis=1)

    print("\n--- Таблиця студентів та їх результати ---")
    print(df[["Прізвище", "Ім'я", "Середній бал студента"]].to_string(index=False))
    group_avg = df[subjects].mean().round(2)

    print("\n--- Середній бал групи з дисциплін ---")
    print(group_avg)
    df.to_csv(FILENAME, index=False, encoding='utf-8-sig')
    print(f"\nРезультати оновлено у файлі {FILENAME}.")

if __name__ == "__main__":
    handle_students_pandas()