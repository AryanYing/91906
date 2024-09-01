# 3PAD Maths Quiz
# Date: 1/08/24
# Author: Aryan Ying

# Import required libraries
import tkinter as tk  # GUI library for Python
from tkinter import messagebox  # Import messagebox from tkinter for showing pop-up messages
from sympy import *  # Library for symbolic mathematics
import sys  # Provides access to system-specific parameters and functions
import random  # Generates random numbers
import mpmath  # Library for floating-point arithmetic
import json  # Library for handling JSON files
sys.modules['sympy.mpmath'] = mpmath  # Link mpmath with sympy to avoid conflicts

# Create login credentials
VALID_USERNAME = "user"  # Valid username for login
VALID_PASSWORD = "pass"  # Valid password for login

# Define the login window
class LoginApp:
    def __init__(self, master):
        # Initialize the login window
        self.master = master
        self.master.title("Login")  # Set the title of the window
        self.master.geometry("300x250")  # Set the window size
        self.master.resizable(False, False)  # Prevent resizing
        
        # Username label and entry field
        self.username_label = tk.Label(self.master, text="Username:")  # Label for the username
        self.username_label.pack(pady=5)  # Place the label in the window
        
        self.username_entry = tk.Entry(self.master)  # Input field for the username
        self.username_entry.pack(pady=5)  # Place the input field in the window
        
        # Password label and entry field
        self.password_label = tk.Label(self.master, text="Password:")  # Label for the password
        self.password_label.pack(pady=5)  # Place the label in the window
        
        self.password_entry = tk.Entry(self.master, show='*')  # Input field for the password (hidden)
        self.password_entry.pack(pady=5)  # Place the input field in the window
        
        # Login button
        self.login_btn = tk.Button(self.master, text="Login", command=self.validate_login)  # Button for login
        self.login_btn.pack(pady=20)  # Place the button in the window

        # Signup button
        self.signup_btn = tk.Button(self.master, text="Signup", command=self.validate_signup)  # Button for signup
        self.signup_btn.pack()  # Place the button in the window
    
    # Validate login credentials
    def validate_login(self):
        username = self.username_entry.get()  # Get the username from the entry field
        password = self.password_entry.get()  # Get the password from the entry field
        
        # Open the JSON file containing user details
        with open("users.json", "r") as r:
            users = json.load(r)  # Load users from JSON file

            # Check if the entered username and password match any user in the file
            for user in users:
                if user["name"] == username and user["pass"] == password:
                    messagebox.showinfo("Success", "Login successful!")  # Show success message
                    self.master.destroy()  # Close the login window
                    global root
                    root = tk.Tk()  # Create the main quiz window
                    MathsGame(root)  # Start the math quiz
                    return
                
            messagebox.showerror("Error", "Invalid credentials.")  # Show error message if login fails

    # Validate signup process
    def validate_signup(self):
        username = self.username_entry.get()  # Get the username from the entry field
        password = self.password_entry.get()  # Get the password from the entry field
        
        # Check username and password length and validity
        if len(username) < 4 and username.isalpha:  # Check if username is alphabetical and long enough
            messagebox.showinfo(message="Username must be alphabetical and 4 or more.")  # Show error message
            return
        if len(password) < 4:  # Check if password is long enough
            messagebox.showinfo(message="Password must be length 4 or more.")  # Show error message
            return

        # Open the JSON file containing user details
        with open("users.json", "r") as r:
            users = json.load(r)  # Load users from JSON file

            # Check if the username already exists
            for user in users:
                if user["name"] == username:
                    messagebox.showerror("Error", "This user exists already.")  # Show error if user exists
                    return
                    
            # Add new user account
            users.append({"name": username, "pass": password})  # Append the new user details

            # Save the updated user list to the JSON file
            with open("users.json", "w") as w:
                json.dump(users, w, indent=2)  # Write users to file with indentation
                messagebox.showinfo("Success", "Signup successful!")  # Show success message
                self.master.destroy()  # Close the signup window
                global root
                root = tk.Tk()  # Create the main quiz window
                MathsGame(root)  # Start the math quiz
                return
            

class MathsGame:
    # Design the main window for the math quiz
    def __init__(self, master):
        self.master = master
        self.master.title("Maths game")  # Set the title of the window
        self.master.geometry("400x300")  # Set the window size
        self.master.resizable(False, False)  # Prevent resizing
        self.in_game = False  # Flag to track if a game is in progress

        # Banner at the top of the window
        self.banner_label = tk.Label(self.master, text="Math Game", font=("Calibri", 24, "bold"), bg="lightblue", fg="Purple")  # Banner label
        self.banner_label.pack(fill=tk.X)  # Place the banner
        
        # Welcome label
        self.welcome_label = tk.Label(self.master, text="Welcome to the Main Application!")  # Welcome message
        self.welcome_label.pack(pady=20)  # Place the label

        # Beginner level button
        self.beginner_btn = tk.Button(self.master, text="Beginner", command=lambda: self.open_quiz(0))  # Beginner quiz button
        self.beginner_btn.pack(pady=5)  # Place the button
        
        # Intermediate level button
        self.intermediate_btn = tk.Button(self.master, text="Intermediate", command=lambda: self.open_quiz(1))  # Intermediate quiz button
        self.intermediate_btn.pack(pady=5)  # Place the button
        
        # Advanced level button
        self.advanced_btn = tk.Button(self.master, text="Advanced", command=lambda: self.open_quiz(2))  # Advanced quiz button
        self.advanced_btn.pack(pady=5)  # Place the button
        
        self.master.mainloop()  # Start the main loop of the window
    
    # Generate beginner level questions
    def generate_question_beginner(self):
        if self.question_count < 20:  # Check if the question count is less than 20
            self.question_count += 1  # Increment the question count
            num1 = random.randint(1, 10)  # Generate a random number between 1 and 10
            num2 = random.randint(1, 10)  # Generate another random number between 1 and 10
            operation = random.choice(['+', '-'])  # Choose a random operation
            
            # Determine the correct answer based on the operation
            if operation == '+':
                self.correct_answer = num1 + num2
            else:
                self.correct_answer = num1 - num2
            
            # Create the question string
            question = f"Question {self.question_count}: {num1} {operation} {num2} = ?"
            
            # Display the question on the quiz window
            if hasattr(self, 'question_label'):
                self.question_label.config(text=question)  # Update the question label
            else:
                self.question_label = tk.Label(self.quiz_window, text=question, font=("Calibri", 18))  # Create a question label
                self.question_label.pack(pady=20)  # Place the label
            
            # Create the answer entry field
            if hasattr(self, 'answer_entry'):
                self.answer_entry.delete(0, tk.END)  # Clear the existing answer
            else:
                self.answer_entry = tk.Entry(self.quiz_window)  # Create an entry field for answers
                self.answer_entry.pack(pady=10)  # Place the entry field
            
            # Create the submit button
            if hasattr(self, 'submit_btn'):
                self.submit_btn.config(command=self.check_answer_beginner)  # Update button command
            else:
                self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=self.check_answer_beginner)  # Create a submit button
                self.submit_btn.pack(pady=20)  # Place the button
        else:
            self.end_quiz()  # End the quiz after 20 questions
    
    # Check the beginner level answer
    def check_answer_beginner(self):
        try:
            user_answer = int(self.answer_entry.get())  # Get the user answer as an integer
            if user_answer == self.correct_answer:  # Check if the answer is correct
                self.correct_answers += 1  # Increment the correct answers count
                self.gif()  # Display a GIF animation
            
            self.generate_question_beginner()  # Generate the next question
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")  # Show error if input is not a number

    # Generate intermediate level questions
    def generate_question_intermediate(self):
        if self.question_count < 20:  # Check if the question count is less than 20
            self.question_count += 1  # Increment the question count
            num1 = random.randint(1, 10)  # Generate a random number between 1 and 10
            num2 = random.randint(1, 10)  # Generate another random number between 1 and 10
            operation = random.choice(['*', '/'])  # Choose a random operation
            
            # Determine the correct answer based on the operation
            if operation == '*':
                self.correct_answer = num1 * num2
            else:
                self.correct_answer = round(num1 / num2, 2)  # Round to 2 decimal places
            
            # Create the question string
            question = f"Question {self.question_count}: {num1} {operation} {num2} = ?"
            
            # Display the question on the quiz window
            if hasattr(self, 'question_label'):
                self.question_label.config(text=question)  # Update the question label
            else:
                self.question_label = tk.Label(self.quiz_window, text=question, font=("Calibri", 18))  # Create a question label
                self.question_label.pack(pady=20)  # Place the label
            
            # Create the answer entry field
            if hasattr(self, 'answer_entry'):
                self.answer_entry.delete(0, tk.END)  # Clear the existing answer
            else:
                self.answer_entry = tk.Entry(self.quiz_window)  # Create an entry field for answers
                self.answer_entry.pack(pady=10)  # Place the entry field
            
            # Create the submit button
            if hasattr(self, 'submit_btn'):
                self.submit_btn.config(command=self.check_answer_intermediate)  # Update button command
            else:
                self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=self.check_answer_intermediate)  # Create a submit button
                self.submit_btn.pack(pady=20)  # Place the button
        else:
            self.end_quiz()  # End the quiz after 20 questions
    
    # Check the intermediate level answer
    def check_answer_intermediate(self):
        try:
            user_answer = float(self.answer_entry.get())  # Get the user answer as a float
            if round(user_answer, 2) == self.correct_answer:  # Check if the answer is correct (rounded)
                self.correct_answers += 1  # Increment the correct answers count
                self.gif()  # Display a GIF animation

            self.generate_question_intermediate()  # Generate the next question
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")  # Show error if input is not a number

    # Create the quiz window
    def open_quiz(self, diff):
        if self.in_game == True:  # Check if a game is already in progress
            return messagebox.showerror(message="Finish your current game.")  # Show error message
        self.in_game = True  # Set the in-game flag to True
        self.quiz_window = tk.Toplevel(self.master)  # Create a new top-level window for the quiz
        self.quiz_window.title("Quiz")  # Set the title of the quiz window
        self.quiz_window.geometry("800x500")  # Set the size of the quiz window
        self.quiz_window.resizable(False, False)  # Prevent resizing
        
        self.quiz_window.protocol("WM_DELETE_WINDOW", lambda: on_closing())  # Disable close button during the game

        # Function to handle the window closing event
        def on_closing():
            messagebox.showinfo(message="Please finish the 20 question game first.")  # Show message on close attempt

        # Create labels and buttons for quiz window
        self.question_label = tk.Label(self.quiz_window, text="", font=("Calibri", 18))  # Label to display questions
        self.question_label.pack(pady=20)  # Place the label

        self.answer_entry = tk.Entry(self.quiz_window)  # Entry field for user's answer
        self.answer_entry.pack(pady=10)  # Place the entry field

        self.submit_btn = tk.Button(self.quiz_window, text="Submit", command=lambda: submit())  # Submit button
        self.submit_btn.pack(pady=20)  # Place the button

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
        
        # Start the quiz based on difficulty level
        if diff == 0:
            self.generate_question_beginner()  # Start beginner quiz
        elif diff == 1:
            self.generate_question_intermediate()  # Start intermediate quiz
        else:
            self.generate_question_advanced()  # Start advanced quiz

        # Handle the submit button action
        def submit():
            if diff == 0:
                self.check_answer_beginner()  # Check beginner answer
            elif diff == 1:
                self.check_answer_intermediate()  # Check intermediate answer
            else:
                self.check_answer_advanced()  # Check advanced answer

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
    
    # Generate advanced level questions
    def generate_question_advanced(self):
        if self.question_count < 20:  # Check if the question count is less than 20
            self.question_count += 1  # Increment the question count
            x = symbols('x')  # Define a symbolic variable x
            operation = random.choice(['diff', 'integrate'])  # Randomly choose differentiation or integration
            expr = random.choice([x**2 + 2*x + 1, sin(x), cos(x), exp(x), x**3])  # Randomly select a mathematical expression
            
            # Set the question based on the operation
            if operation == 'diff':
                self.correct_answer = diff(expr, x)  # Differentiate the expression
                question = f"Question {self.question_count}: Differentiate {expr} with respect to x"  # Create question
            else:
                self.correct_answer = integrate(expr, x)  # Integrate the expression
                question = f"Question {self.question_count}: Integrate {expr} with respect to x"  # Create question
            
            self.question_label.config(text=question)  # Update the question label

            self.answer_entry.delete(0, tk.END)  # Clear the answer entry field
                
            self.submit_btn.config(command=self.check_answer_advanced)  # Set the submit button command
                
        else:
            self.end_quiz()  # End the quiz after 20 questions
    
    # Check the advanced level answer
    def check_answer_advanced(self):
        try:
            user_answer = sympify(self.answer_entry.get())  # Convert user input to a symbolic expression
            if simplify(user_answer - self.correct_answer) == 0:  # Check if the user's answer matches the correct one
                self.correct_answers += 1  # Increment the correct answers count
                self.gif()  # Display a GIF animation
            
            self.generate_question_advanced()  # Generate the next question
        except (SympifyError, ValueError):
            messagebox.showerror("Error", "Please enter a valid expression.")  # Show error if input is not a valid expression
    
    # End the quiz and display results
    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"You answered {self.correct_answers} out of 20 questions correctly!")  # Show quiz results
        self.in_game = False  # Reset the in-game flag
        self.quiz_window.destroy()  # Close the quiz window

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = LoginApp(root)  # Initialize the login application
    root.mainloop()  # Run the main event loop
