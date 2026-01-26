company_data = {
    "company_name": "ІПЗ-33",
    "employees": [  
        {
            "id": 101, 
            "name": "Danylo", 
            "skills": ["Python", "HTML & CSS", "JS"]
        },
        {
            "id": 102, 
            "name": "Dmytro", 
            "skills": ["Design", "Figma","Python","C++"]
        }
    ]
}
print("--- Навігація по вкладеності ---")
all_employees = company_data["employees"]
first_worker = all_employees[0] 

print(f"Студент: {first_worker['name']}")
worker_skills = first_worker["skills"]
target_skill = worker_skills[1]

print(f"Навичка: {target_skill}")
quick_access = company_data["employees"][0]["skills"][1]
print(f"Швидкий доступ: {quick_access}")