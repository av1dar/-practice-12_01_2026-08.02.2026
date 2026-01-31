def analyze_grades(students_data):
    average_scores = {}
    all_grades_raw = []

    print("--- Розрахунків --")
    for name, grades in students_data.items():
        if len(grades) > 0:
            avg = sum(grades) / len(grades)
            average_scores[name] = round(avg, 2)
            all_grades_raw.extend(grades)
            print(f"Студент {name}: оцінки {grades} -> сер. бал {avg:.2f}")
        else:
            average_scores[name] = 0.0
    unique_grades = set(all_grades_raw)
    return average_scores, unique_grades
input_data = {
    "Андрій": [88, 90, 80, 90],
    "Олена": [94, 100, 96, 93],  
    "Максим": [67, 79, 68, 75]   
}
final_dict, unique_set = analyze_grades(input_data)

print("\n--- Результати ---")
print(f"Словник середніх балів: {final_dict}")
print(f"Кількість унікальних оцінок: {len(unique_set)}")
print(f"Самі унікальні оцінки (set): {unique_set}")