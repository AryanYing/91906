import tkinter as tk
from tkinter import messagebox
from sympy import *
import sys
import mpmath
sys.modules['sympy.mpmath'] = mpmath


VALID_USERNAME = "user"
VALID_PASSWORD = "pass"

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")
        
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)
        
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.pack(pady=5)
        
        self.login_btn = tk.Button(self.master, text="Login", command=self.validate_login)
        self.login_btn.pack(pady=20)
    
    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()
            self.open_main_window()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
    
    def open_main_window(self):
        self.main_window = tk.Tk()
        self.main_window.title("Main Application")
        self.main_window.geometry("400x300")
        
        # Banner
        self.banner_label = tk.Label(self.main_window, text="Math Game", font=("Arial", 24, "bold"), bg="blue", fg="white")
        self.banner_label.pack(fill=tk.X)
        
        self.welcome_label = tk.Label(self.main_window, text="Welcome to the Main Application!")
        self.welcome_label.pack(pady=20)
        
        self.main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
