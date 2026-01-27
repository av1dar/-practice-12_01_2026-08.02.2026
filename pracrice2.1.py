
import tkinter as tk
root = tk.Tk()

root.title("ЗЕЛЯ ТЕЛЕХВОН") 
root.geometry("500x400")             

label_hello = tk.Label(root, text="Привіт! Це ТЦК", font=("Arial", 20))
btn_click = tk.Button(root, text="Оновити дані в Резер+", bg="yellow")
label_hello.pack(pady=20)  
btn_click.pack()
print("Програма запустилася і чекає...")

root.mainloop()
print("Програма завершила роботу.") 