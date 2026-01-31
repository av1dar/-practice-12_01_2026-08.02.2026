class Student:
    def __init__(self, name, group, average_score):
    

        self.name = name
        self.group = group
        self.average_score = average_score
    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Група: {self.group}")
        print(f"Середній бал: {self.average_score}")
        print("-" * 15)  

student1 = Student("Олександр Шевченко", "ІПЗ-21", 4)
student2 = Student("Марія Кізяк", "ЖК-12", 4.7)
student3 = Student("Дмитро Коляденко", "ІПЗ-33", 5)
print("Список групи\n")
student1.show_info()
student2.show_info()
student3.show_info()