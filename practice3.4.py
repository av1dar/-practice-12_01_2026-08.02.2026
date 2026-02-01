import tkinter as tk

def calculate(operation):
    """
    Функція виконує арифметичну дію залежно від переданого знаку (+, -, *, /).
    """
    try:
        val1 = entry_num1.get().replace(',', '.')
        val2 = entry_num2.get().replace(',', '.')
        num1 = float(val1)
        num2 = float(val2)
        
        result = 0
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                label_result.config(text="Помилка: Ділення на нуль!", fg="red")
                return 
            result = num1 / num2
        label_result.config(text=f"Результат: {round(result, 3)}", fg="green")

    except ValueError:

        label_result.config(text="Помилка: Введіть коректні числа!", fg="red")
root = tk.Tk()
root.title("Міні-калькулятор")
root.geometry("500x500")

tk.Label(root, text="Перше число:").pack(pady=20),
entry_num1 = tk.Entry(root)
entry_num1.pack()
tk.Label(root, text="Друге число:").pack(pady=20),
entry_num2 = tk.Entry(root)
entry_num2.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=15)

btn_plus = tk.Button(buttons_frame, text="+", width=5, command=lambda: calculate("+"))
btn_plus.grid(row=0, column=0, padx=5)

btn_minus = tk.Button(buttons_frame, text="-", width=5, command=lambda: calculate("-"))
btn_minus.grid(row=0, column=1, padx=5)

btn_mul = tk.Button(buttons_frame, text="*", width=5, command=lambda: calculate("*"))
btn_mul.grid(row=0, column=2, padx=5)

btn_div = tk.Button(buttons_frame, text="/", width=5, command=lambda: calculate("/"))
btn_div.grid(row=0, column=3, padx=5)

label_result = tk.Label(root, text="Результат з'явиться тут", font=("Arial", 25, "bold"))
label_result.pack(pady=20)

root.mainloop()