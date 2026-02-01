import tkinter as tk
from tkinter import messagebox
import logic  

class CurrencyConverterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер валют (MVC)")
        self.root.geometry("300x200")
        tk.Label(root, text="Сума в USD ($):").pack(pady=5)
        self.entry_amount = tk.Entry(root)
        self.entry_amount.pack()

        tk.Label(root, text="Курс (грн за 1$):").pack(pady=5)
        self.entry_rate = tk.Entry(root)
        self.entry_rate.pack()
        
        self.btn_calc = tk.Button(root, text="Перевести в UAH", command=self.on_calculate)
        self.btn_calc.pack(pady=15)
        
        self.label_result = tk.Label(root, text="0.00 грн", font=("Arial", 14, "bold"), fg="blue")
        self.label_result.pack()

    def on_calculate(self):
        """Функція-посередник: бере дані з UI -> передає в Logic -> повертає в UI"""
        amount_text = self.entry_amount.get()
        rate_text = self.entry_rate.get()

        result = logic.convert_currency(amount_text, rate_text)

        if result is None:
            messagebox.showerror("Помилка", "Введіть коректні додатні числа!")
            self.label_result.config(text="Помилка")
        else:
            self.label_result.config(text=f"{result:.2f} грн")