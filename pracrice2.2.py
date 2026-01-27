import tkinter as tk
root = tk.Tk()
root.geometry("500x300")

count = 0
def on_button_click():
    global count 
    count += 1
   
    label.config(text=f"Кліків: {count}")
    print(f"Подія спрацювала! Лічильник: {count}")

label = tk.Label(root, text="Кліків: 0", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(root, text="ТАПАЙ!", command=on_button_click, bg="lightblue")
btn.pack()
root.mainloop()