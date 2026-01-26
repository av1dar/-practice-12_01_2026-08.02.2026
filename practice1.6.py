#1
def create_profile(username, role="Guest"):
    print(f"Створено профіль: {username} (Роль: {role})")
create_profile("daniik")             
create_profile("Admin", "SuperUser") 

#2
def modify_data(number, my_list):
    number = 999          
    my_list.append("New") 
a = 10
b = ["Start"]
modify_data(a, b)
print(f"Число: {a}") 
print(f"Список: {b}")  

#3
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Факторіал 5!: {factorial(5)}")

#4
def security_check(func):
    def wrapper():
        password = input("Введіть пароль (admin): ")
        if password == "admin":
            print("Доступ надано.")
            func() 
        else:
            print("Доступ заборонено!")
    return wrapper
@security_check
def open_secret_document():
    print(">>> ВМІСТ ЦІЛКОМ ТАЄМНОГО ДОКУМЕНТА <<<")
open_secret_document()

#5
class Counter:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        print(f"Викликано разів: {self.count}")
my_clicker = Counter()
my_clicker() 
my_clicker() 
my_clicker() 
 