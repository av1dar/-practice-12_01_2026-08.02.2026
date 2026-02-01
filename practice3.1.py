import tkinter as tk 

def create_app():
    root = tk.Tk()

    root.title("Перша програма")
    
    root.geometry("1024x768")
    
    root.resizable(False, False)

    label = tk.Label(root, text="Hello, world!", font=("Arial", 24))
    label.pack(pady=50)
    close_button = tk.Button(root, text="Закрити", font=("Arial", 14), command=root.destroy)
    close_button.pack(pady=20)
    root.mainloop()
if __name__ == "__main__":
    create_app()