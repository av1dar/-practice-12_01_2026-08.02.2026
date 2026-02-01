import tkinter as tk

def save_data():
    """Функція обробки натискання кнопки 'Зберегти'"""
    name = name_var.get()
    gender = gender_var.get()
    is_agreed = agree_var.get()
    if not is_agreed:
        result_label.config(text="Помилка: Ви маєте погодитись із умовами!", fg="red")
        return

    if not name.strip():
        result_label.config(text=" Халепа: Введіть ім'я!", fg="red")
        return
    info_text = f"Дані збережено:\nІм'я: {name}\nСтать: {gender}"
    result_label.config(text=info_text, fg="green")

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("350x300")

name_var = tk.StringVar()
gender_var = tk.StringVar(value="Не вказано") 
agree_var = tk.BooleanVar()

label_name = tk.Label(root, text="Ваше ім'я:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w") 

entry_name = tk.Entry(root, textvariable=name_var)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_gender = tk.Label(root, text="Стать:")
label_gender.grid(row=1, column=0, padx=10, pady=5, sticky="w")
rb_male = tk.Radiobutton(root, text="Чоловіча", variable=gender_var, value="Чоловік")
rb_male.grid(row=1, column=1, sticky="w")

rb_female = tk.Radiobutton(root, text="Жіноча", variable=gender_var, value="Жінка")
rb_female.grid(row=2, column=1, sticky="w")
check_agree = tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=agree_var, onvalue=True, offvalue=False)
check_agree.grid(row=3, column=0, columnspan=2, pady=10)
btn_save = tk.Button(root, text="Зберегти", command=save_data, width=20, bg="#dddddd")
btn_save.grid(row=4, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()