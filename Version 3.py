#3PAD Maths Quiz
#Date:1/08/24
#Author: Aryan Ying

#Import libraries 
import tkinter as tk
from tkinter import messagebox
from sympy import *
import sys
import random
import mpmath
sys.modules['sympy.mpmath'] = mpmath

#Create login details
VALID_USERNAME = "user"
VALID_PASSWORD = "pass"

#Make the login window
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
    #Make the login in detials valid 
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
    #Design the main window for the maths quiz
    def open_main_window(self):
        self.main_window = tk.Tk()
        self.main_window.title("Main Application")
        self.main_window.geometry("400x300")
        
        # Banner
        self.banner_label = tk.Label(self.main_window, text="Math Game", font=("Arial", 24, "bold"), bg="blue", fg="white")
        self.banner_label.pack(fill=tk.X)
        
        self.welcome_label = tk.Label(self.main_window, text="Welcome to the Main Application!")
        self.welcome_label.pack(pady=20)
        
        # Add buttons
        self.beginner_btn = tk.Button(self.main_window, text="Beginner", command=self.open_beginner_quiz)
        self.beginner_btn.pack(pady=5)
        
        self.intermediate_btn = tk.Button(self.main_window, text="Intermediate", command=self.open_intermediate_quiz)
        self.intermediate_btn.pack(pady=5)
        
        self.advanced_btn = tk.Button(self.main_window, text="Advanced", command=self.open_advanced_quiz)
        self.advanced_btn.pack(pady=5)
        
        self.main_window.mainloop()

        # Canvas to display animations
        self.animation_canvas = tk.Canvas(self.quiz_window, width=800, height=320, bg="grey33")  # Canvas for GIFs
        self.animation_canvas.pack()  # Place the canvas
        self.anim_one_index = 0  # Index for first animation frame
        self.anim_two_index = 0  # Index for second animation frame
        self.char_one = tk.PhotoImage(file="enemy.gif", format="gif -index " + str(self.anim_one_index))  # Load first GIF
        self.char_two = tk.PhotoImage(file="archer.gif", format="gif -index " + str(self.anim_two_index))  # Load second GIF
        self.animation_canvas.create_image(-100, -100, image=self.char_one, anchor="nw")  # Display first GIF
        self.animation_canvas.create_image(150, 30, image=self.char_two, anchor="nw")  # Display second GIF

        self.question_count = 0  # Initialize question count
        self.correct_answers = 0  # Initialize correct answers count
    #Create the beginner quiz``     ``--
    def open_beginner_quiz(self):
        self.quiz_window = tk.Toplevel(self.main_window)
        self.quiz_window.title("Beginner Quiz")
        self.quiz_window.geometry("400x300")
        
        self.question_count = 0
        self.correct_answers = 0
        
        self.generate_question_beginner()
    
    def generate_question_beginner(self):
        if self.question_count < 20:
            self.question_count += 1
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(['+', '-'])
            
            if operation == '+':
                self.correct_answer = num1 + num2
            else:
                self.correct_answer = num1 - num2
            
            question = f"Question {self.question_count}: {num1} {operation} {num2} = ?"
            
            if hasattr(self, 'question_label'):
                self.question_label.config(text=question)
            else:
                self.question_label = tk.Label(self.quiz_window, text=question, font=("Arial", 18))
                self.question_label.pack(pady=20)
            
            if hasattr(self, 'answer_entry'):
                self.answer_entry.delete(0, tk.END)
            else:
                self.answer_entry = tk.Entry(self.quiz_window)
                self.answer_entry.pack(pady=10)
            
            if hasattr(self, 'submit_btn'):
                self.submit_btn.config(command=self.check_answer_beginner)
            else:
                self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=self.check_answer_beginner)
                self.submit_btn.pack(pady=20)
        else:
            self.end_quiz()
    
    def check_answer_beginner(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.correct_answers += 1
            
            self.generate_question_beginner()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    #Create the intermediate quiz
    def open_intermediate_quiz(self):
        self.quiz_window = tk.Toplevel(self.main_window)
        self.quiz_window.title("Intermediate Quiz")
        self.quiz_window.geometry("400x300")
        
        self.question_count = 0
        self.correct_answers = 0
        
        self.generate_question_intermediate()
    
    def generate_question_intermediate(self):
        if self.question_count < 20:
            self.question_count += 1
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(['*', '/'])
            
            if operation == '*':
                self.correct_answer = num1 * num2
            else:
                self.correct_answer = round(num1 / num2, 2)
            
            question = f"Question {self.question_count}: {num1} {operation} {num2} = ?"
            
            if hasattr(self, 'question_label'):
                self.question_label.config(text=question)
            else:
                self.question_label = tk.Label(self.quiz_window, text=question, font=("Arial", 18))
                self.question_label.pack(pady=20)
            
            if hasattr(self, 'answer_entry'):
                self.answer_entry.delete(0, tk.END)
            else:
                self.answer_entry = tk.Entry(self.quiz_window)
                self.answer_entry.pack(pady=10)
            
            if hasattr(self, 'submit_btn'):
                self.submit_btn.config(command=self.check_answer_intermediate)
            else:
                self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=self.check_answer_intermediate)
                self.submit_btn.pack(pady=20)
        else:
            self.end_quiz()
    
    def check_answer_intermediate(self):
        try:
            user_answer = float(self.answer_entry.get())
            if round(user_answer, 2) == self.correct_answer:
                self.correct_answers += 1
            
            self.generate_question_intermediate()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

            # Display GIF animation
    def gif(self):
        # Function to animate the first GIF
        def gif_one():
            try:
                self.char_one = tk.PhotoImage(file="enemy.gif", format="gif -index " + str(self.anim_one_index))  # Load GIF frame
                self.animation_canvas.create_image(-100, -100, image=self.char_one, anchor="nw")  # Display GIF frame
                self.anim_one_index += 1  # Increment frame index
                self.master.after(50, gif_one)  # Delay and repeat animation
            except Exception:
                self.anim_one_index = 0  # Reset index on error

        # Function to animate the second GIF
        def gif_two():
            try:
                self.char_two = tk.PhotoImage(file="archer.gif", format="gif -index " + str(self.anim_two_index))  # Load GIF frame
                self.animation_canvas.create_image(150, 30, image=self.char_two, anchor="nw")  # Display GIF frame
                self.anim_two_index += 1  # Increment frame index
                self.master.after(50, gif_two)  # Delay and repeat animation
            except Exception:
                self.anim_two_index = 0  # Reset index on error

        self.master.after(800, gif_one)  # Start first animation after delay
        gif_two()  # Start second animation immediately
        
    #Create the advanced quiz
    def open_advanced_quiz(self):
        self.quiz_window = tk.Toplevel(self.main_window)
        self.quiz_window.title("Advanced Quiz")
        self.quiz_window.geometry("800x300")
        
        self.question_count = 0
        self.correct_answers = 0
        
        self.generate_question_advanced()
    
    def generate_question_advanced(self):
        if self.question_count < 20:
            self.question_count += 1
            x = symbols('x')
            operation = random.choice(['diff', 'integrate'])
            expr = random.choice([x**2 + 2*x + 1, sin(x), cos(x), exp(x), x**3])
            
            if operation == 'diff':
                self.correct_answer = diff(expr, x)
                question = f"Question {self.question_count}: Differentiate {expr} with respect to x"
            else:
                self.correct_answer = integrate(expr, x)
                question = f"Question {self.question_count}: Integrate {expr} with respect to x"
            
            if hasattr(self, 'question_label'):
                self.question_label.config(text=question)
            else:
                self.question_label = tk.Label(self.quiz_window, text=question, font=("Arial", 18))
                self.question_label.pack(pady=20)
            
            if hasattr(self, 'answer_entry'):
                self.answer_entry.delete(0, tk.END)
            else:
                self.answer_entry = tk.Entry(self.quiz_window)
                self.answer_entry.pack(pady=10)
            
            if hasattr(self, 'submit_btn'):
                self.submit_btn.config(command=self.check_answer_advanced)
            else:
                self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=self.check_answer_advanced)
                self.submit_btn.pack(pady=20)
        else:
            self.end_quiz()
    
    def check_answer_advanced(self):
        try:
            user_answer = sympify(self.answer_entry.get())
            if simplify(user_answer - self.correct_answer) == 0:
                self.correct_answers += 1
            
            self.generate_question_advanced()
        except (SympifyError, ValueError):
            messagebox.showerror("Error", "Please enter a valid expression.")
    
    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"You answered {self.correct_answers} out of 20 questions correctly!")
        self.quiz_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
