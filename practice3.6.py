import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Мій Блокнот")
        self.root.geometry("800x600")
        
        self.file_path = None
        self.is_modified = False
        
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(root, font=("Arial", 14), yscrollcommand=self.scrollbar.set, undo=True)
        self.text_area.pack(expand=True, fill="both")
        
        self.scrollbar.config(command=self.text_area.yview)
        
        self.text_area.bind("<KeyRelease>", self.mark_as_modified)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)

        self.file_menu.add_command(label="Відкрити", command=self.open_file)
        self.file_menu.add_command(label="Зберегти", command=self.save_file)
        self.file_menu.add_separator() 
        self.file_menu.add_command(label="Вийти", command=self.on_closing)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def mark_as_modified(self, event=None):
        """Викликається, коли користувач щось друкує"""
        if not self.is_modified:
            self.is_modified = True
            current_title = self.root.title()
            if not current_title.startswith("*"):
                self.root.title("*" + current_title) 

    def open_file(self):
        """Відкриває файл"""
        if self.is_modified:
            answer = messagebox.askyesno("Увага", "У вас є незбережені зміни. Відкрити інший файл?")
            if not answer:
                return

        path = filedialog.askopenfilename(defaultextension=".txt",
         filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if path:
            self.file_path = path
            self.text_area.delete(1.0, tk.END)
            
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.insert(1.0, content)
            
            self.root.title(f"Мій Блокнот - {path}")
            self.is_modified = False

    def save_file(self):
        """Зберігає файл"""
        if self.file_path:
            path = self.file_path
        else:
            path = filedialog.asksaveasfilename(defaultextension=".txt",
          filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        
        if path:
            try:
                content = self.text_area.get(1.0, tk.END) 
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                
                self.file_path = path
                self.root.title(f"Мій Блокнот - {path}")
                self.is_modified = False
                return True 
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {e}")
                return False
        return False

    def on_closing(self):
        """Функція при спробі закрити програму"""
        if self.is_modified:
            answer = messagebox.askyesnocancel("Вихід", "Зберегти зміни перед виходом?")
            
            if answer is True:  
                if self.save_file():
                    self.root.destroy() 
            elif answer is False: 
                self.root.destroy() 
            else: 
                pass 
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()