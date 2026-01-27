import tkinter as tk

root = tk.Tk()
root.title("Анкета співробітника")
root.geometry("400x400")


tk.Label(root, text="Ім'я:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Прізвище:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_surname = tk.Entry(root)
entry_surname.grid(row=1, column=1, padx=10, pady=5)


tk.Label(root, text="Відділ:").grid(row=2, column=0, sticky="w", padx=10)


dept_var = tk.IntVar()
dept_var.set(1)

rb1 = tk.Radiobutton(root, text="IT Відділ", variable=dept_var, value=1)
rb1.grid(row=2, column=1, sticky="w")

rb2 = tk.Radiobutton(root, text="Бухгалтерія", variable=dept_var, value=2)
rb2.grid(row=3, column=1, sticky="w")

agree_var = tk.BooleanVar() 
check = tk.Checkbutton(root, text="Я погоджуюсь на обробку даних", variable=agree_var)

check.grid(row=4, column=0, columnspan=2, pady=10)

def submit():
    name = entry_name.get()
    dept = "IT" if dept_var.get() == 1 else "Бухгалтерія"
    agreed = "Так" if agree_var.get() else "Ні"
    
    print(f"Дані: {name}, Відділ: {dept}, Згода: {agreed}")

btn = tk.Button(root, text="Відправити", command=submit, bg="#dddddd")
btn.grid(row=5, column=0, columnspan=2, pady=10, ipadx=20)

root.mainloop()