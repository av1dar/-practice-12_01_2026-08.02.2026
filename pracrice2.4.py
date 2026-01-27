import tkinter as tk

def convert_currency():
    try:
  
        uah_text = entry_uah.get()
        
        
        uah_amount = float(uah_text) 
        
        exchange_rate = 41
        usd_amount = uah_amount / exchange_rate
        
   
        usd_amount = round(usd_amount, 2)
        
   
        result_label.config(text=f"{usd_amount} $", fg="green")
        
    except ValueError:
       
        result_label.config(text="Введіть число!", fg="red")

root = tk.Tk()
root.title("Обмінник")
root.geometry("250x200")

tk.Label(root, text="Сума в гривнях (UAH):").pack(pady=10)

entry_uah = tk.Entry(root, justify="center") 
entry_uah.pack()

btn_calc = tk.Button(root, text="Конвертувати", command=convert_currency, bg="#f0f0f0")
btn_calc.pack(pady=10)

result_label = tk.Label(root, text="---", font=("Arial", 20, "bold"))
result_label.pack(pady=20)

root.bind('<Return>', lambda event: convert_currency())

root.mainloop()