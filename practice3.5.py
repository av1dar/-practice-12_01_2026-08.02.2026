import tkinter as tk
from tkinter import ttk  
from tkinter import colorchooser 
import json
import os

CONFIG_FILE = "settings.json"

def load_settings():
    """Завантажує колір з файлу. Якщо файлу немає — повертає стандартний сірий."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("bg_color", "#f0f0f0")
        except:
            return "#f0f0f0"
    return "#f0f0f0"

def save_settings(color):
    """Зберігає вибраний колір у файл JSON"""
    data = {"bg_color": color}
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)


def change_color():
    """Відкриває палітру і змінює колір фону"""
    
    color = colorchooser.askcolor(title="Оберіть колір фону")[1]
    
    if color: 
        apply_color(color)
        save_settings(color) 

def apply_color(color):
    """Застосовує колір до всіх вкладок"""
    tab_main.config(bg=color)
    tab_settings.config(bg=color)
    tab_about.config(bg=color)
root = tk.Tk()
root.title("Програма з вкладками")
root.geometry("400x300")
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

current_color = load_settings()
tab_main = tk.Frame(notebook, bg=current_color)
notebook.add(tab_main, text="Головна")

tk.Label(tab_main, text="Введіть дані:", bg=current_color).pack(pady=10)
tk.Entry(tab_main).pack(pady=5)
tk.Button(tab_main, text="Обробити").pack(pady=5)
tab_settings = tk.Frame(notebook, bg=current_color)
notebook.add(tab_settings, text="Налаштування")
tk.Label(tab_settings, text="Налаштування інтерфейсу", font=("Arial", 12), bg=current_color).pack(pady=20)
btn_color = tk.Button(tab_settings, text="Змінити колір фону", command=change_color)
btn_color.pack()
tab_about = tk.Frame(notebook, bg=current_color)
notebook.add(tab_about, text="Про програму")
info_text = "Автор програми: Радченко Данило ІПЗ-33"
tk.Label(tab_about, text=info_text, font=("Courier", 10), bg=current_color).pack(pady=50)
root.mainloop()