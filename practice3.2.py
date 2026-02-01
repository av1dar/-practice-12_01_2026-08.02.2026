import tkinter as tk
def show_greeting():
    """Змінює текст напису на привітання"""
    message_label.config(text="Вітаю, User!", fg="blue")

def clear_text():
    """Очищає текст напису"""
    message_label.config(text="")

root = tk.Tk()
root.title("Керування подіями")
root.geometry("300x250")
message_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
message_label.pack(pady=30)  

btn_greet = tk.Button(root, text="Привітати", font=("Arial", 10), width=15, command=show_greeting)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", font=("Arial", 10), width=15, command=clear_text)
btn_clear.pack(pady=5)
btn_exit = tk.Button(root, text="Вийти", font=("Arial", 10), width=15, bg="#ffdddd", command=root.destroy)
btn_exit.pack(pady=20)

root.mainloop()