
GUI IMPLEMENTATION 1 - PYTHON TUTORIAL
=====================================

This document covers the fundamentals of GUI (Graphical User Interface) development 
in Python using the tkinter library. It includes detailed explanations, examples, 
and practice exercises.

CONTENTS:
1. Introduction to GUI Programming
2. Setting up tkinter
3. Basic GUI Components
4. Event Handling
5. Layout Management
6. Examples (6 comprehensive examples)
7. Practice Exercises (6 exercises with solutions)

=====================================
1. INTRODUCTION TO GUI PROGRAMMING
=====================================

GUI programming allows users to interact with applications through graphical elements
like buttons, text fields, menus, and windows instead of command-line interfaces.

Python's tkinter (Tk interface) is the standard GUI toolkit that comes built-in with Python.
It provides a simple way to create desktop applications with windows, dialogs, and controls.

Key Concepts:
- Widget: A GUI component (button, label, text field, etc.)
- Container: A widget that can hold other widgets (frame, window)
- Event: An action triggered by user interaction (click, key press)
- Event Handler: A function that responds to events
- Layout Manager: Controls how widgets are arranged in containers

=====================================
2. SETTING UP TKINTER
=====================================

tkinter comes pre-installed with Python, so no additional installation is required.

Basic Structure of a tkinter Application:

import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window properties
root.title("My Application")
root.geometry("400x300")  # width x height

# Add widgets here
# ...

# Start the event loop
root.mainloop()

=====================================
3. BASIC GUI COMPONENTS (WIDGETS)
=====================================

Common tkinter Widgets:

1. Label: Displays text or images
   label = tk.Label(root, text="Hello World")

2. Button: Clickable button that triggers actions
   button = tk.Button(root, text="Click Me", command=function_name)

3. Entry: Single-line text input field
   entry = tk.Entry(root)

4. Text: Multi-line text input field
   text = tk.Text(root)

5. Frame: Container for organizing other widgets
   frame = tk.Frame(root)

6. Checkbutton: Checkbox for boolean selections
   checkbutton = tk.Checkbutton(root, text="Option")

7. Radiobutton: Radio button for single selection from multiple options
   radiobutton = tk.Radiobutton(root, text="Choice", variable=var, value=1)

8. Listbox: List of selectable items
   listbox = tk.Listbox(root)

=====================================
4. EVENT HANDLING
=====================================

Events are actions that occur when users interact with the GUI.
Event handlers are functions that respond to these events.

Common Events:
- Button clicks: command parameter
- Key presses: bind("<Key>", function)
- Mouse clicks: bind("<Button-1>", function)
- Window closing: protocol("WM_DELETE_WINDOW", function)

Event Binding Syntax:
widget.bind("<event>", handler_function)

Example Event Handler:
def button_click():
    print("Button was clicked!")

button = tk.Button(root, text="Click", command=button_click)

=====================================
5. LAYOUT MANAGEMENT
=====================================

tkinter provides three geometry managers:

1. Pack: Stacks widgets in blocks
   widget.pack(side=tk.TOP, fill=tk.X, expand=True)

2. Grid: Arranges widgets in rows and columns
   widget.grid(row=0, column=0, sticky="nsew")

3. Place: Positions widgets at absolute coordinates
   widget.place(x=50, y=100)

Grid is most commonly used for complex layouts.

=====================================
6. EXAMPLES
=====================================

EXAMPLE 1: BASIC HELLO WORLD APPLICATION
========================================

def create_hello_world():
    
    # Create main window
    root = tk.Tk()
    
    
    # Set window properties
    root.title("Hello World App")
    
    root.geometry("300x200")
    
    root.configure(bg="lightblue")
    
    
    # Create and pack a label
    label = tk.Label(root, text="Hello, World!", font=("Arial", 16), bg="lightblue")
    
    label.pack(pady=50)
    
    
    # Create and pack a button
    button = tk.Button(root, text="Close", command=root.destroy, font=("Arial", 12))
    
    button.pack(pady=10)
    
    
    # Start the event loop
    root.mainloop()


# Uncomment to run: create_hello_world()


EXAMPLE 2: CALCULATOR WITH BASIC OPERATIONS
==========================================

def create_calculator():
    
    root = tk.Tk()
    
    root.title("Simple Calculator")
    
    root.geometry("300x400")
    
    
    # Variables to store numbers and operation
    num1_var = tk.StringVar()
    
    num2_var = tk.StringVar()
    
    result_var = tk.StringVar()
    
    
    def calculate(operation):
        
        try:
            
            num1 = float(num1_var.get())
            
            num2 = float(num2_var.get())
            
            
            if operation == "add":
                
                result = num1 + num2
                
            elif operation == "subtract":
                
                result = num1 - num2
                
            elif operation == "multiply":
                
                result = num1 * num2
                
            elif operation == "divide":
                
                if num2 != 0:
                    
                    result = num1 / num2
                    
                else:
                    
                    result = "Error: Division by zero"
                    
            
            result_var.set(str(result))
            
        except ValueError:
            
            result_var.set("Error: Invalid input")
    
    
    # Create input fields
    tk.Label(root, text="Number 1:", font=("Arial", 12)).pack(pady=5)
    
    entry1 = tk.Entry(root, textvariable=num1_var, font=("Arial", 12))
    
    entry1.pack(pady=5)
    
    
    tk.Label(root, text="Number 2:", font=("Arial", 12)).pack(pady=5)
    
    entry2 = tk.Entry(root, textvariable=num2_var, font=("Arial", 12))
    
    entry2.pack(pady=5)
    
    
    # Create operation buttons
    button_frame = tk.Frame(root)
    
    button_frame.pack(pady=20)
    
    
    tk.Button(button_frame, text="+", command=lambda: calculate("add"), 
              font=("Arial", 12), width=5).grid(row=0, column=0, padx=5)
    
    tk.Button(button_frame, text="-", command=lambda: calculate("subtract"), 
              font=("Arial", 12), width=5).grid(row=0, column=1, padx=5)
    
    tk.Button(button_frame, text="×", command=lambda: calculate("multiply"), 
              font=("Arial", 12), width=5).grid(row=0, column=2, padx=5)
    
    tk.Button(button_frame, text="÷", command=lambda: calculate("divide"), 
              font=("Arial", 12), width=5).grid(row=0, column=3, padx=5)
    
    
    # Result display
    tk.Label(root, text="Result:", font=("Arial", 12)).pack(pady=(20, 5))
    
    result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), 
                           bg="white", relief="sunken", width=20)
    
    result_label.pack(pady=5)
    
    
    root.mainloop()


# Uncomment to run: create_calculator()


EXAMPLE 3: TO-DO LIST APPLICATION
=================================

def create_todo_app():
    
    root = tk.Tk()
    
    root.title("To-Do List")
    
    root.geometry("400x500")
    
    
    # List to store tasks
    tasks = []
    
    
    def add_task():
        
        task = task_entry.get()
        
        if task:
            
            tasks.append(task)
            
            update_listbox()
            
            task_entry.delete(0, tk.END)
    
    
    def delete_task():
        
        try:
            
            selected_index = task_listbox.curselection()[0]
            
            del tasks[selected_index]
            
            update_listbox()
            
        except IndexError:
            
            pass  # No selection
    
    
    def update_listbox():
        
        task_listbox.delete(0, tk.END)
        
        for task in tasks:
            
            task_listbox.insert(tk.END, task)
    
    
    # Create GUI elements
    tk.Label(root, text="To-Do List", font=("Arial", 16, "bold")).pack(pady=10)
    
    
    # Task entry frame
    entry_frame = tk.Frame(root)
    
    entry_frame.pack(pady=10)
    
    
    task_entry = tk.Entry(entry_frame, font=("Arial", 12), width=25)
    
    task_entry.pack(side=tk.LEFT, padx=5)
    
    
    add_button = tk.Button(entry_frame, text="Add Task", command=add_task, 
                          font=("Arial", 10))
    
    add_button.pack(side=tk.LEFT, padx=5)
    
    
    # Task list
    listbox_frame = tk.Frame(root)
    
    listbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    
    task_listbox = tk.Listbox(listbox_frame, font=("Arial", 10))
    
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    
    scrollbar = tk.Scrollbar(listbox_frame)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    task_listbox.config(yscrollcommand=scrollbar.set)
    
    scrollbar.config(command=task_listbox.yview)
    
    
    # Delete button
    delete_button = tk.Button(root, text="Delete Selected Task", 
                             command=delete_task, font=("Arial", 10))
    
    delete_button.pack(pady=10)
    
    
    # Bind Enter key to add task
    task_entry.bind("<Return>", lambda event: add_task())
    
    
    root.mainloop()


# Uncomment to run: create_todo_app()


EXAMPLE 4: TEXT EDITOR APPLICATION
==================================

from tkinter import filedialog, messagebox


def create_text_editor():
    
    root = tk.Tk()
    
    root.title("Simple Text Editor")
    
    root.geometry("600x500")
    
    
    def new_file():
        
        text_area.delete(1.0, tk.END)
        
        root.title("Simple Text Editor - New File")
    
    
    def open_file():
        
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            
            try:
                
                with open(file_path, 'r') as file:
                    
                    content = file.read()
                    
                    text_area.delete(1.0, tk.END)
                    
                    text_area.insert(1.0, content)
                    
                    root.title(f"Simple Text Editor - {file_path}")
                    
            except Exception as e:
                
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
    
    
    def save_file():
        
        file_path = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            
            try:
                
                with open(file_path, 'w') as file:
                    
                    content = text_area.get(1.0, tk.END)
                    
                    file.write(content)
                    
                    root.title(f"Simple Text Editor - {file_path}")
                    
                    messagebox.showinfo("Success", "File saved successfully!")
                    
            except Exception as e:
                
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
    
    
    # Create menu bar
    menubar = tk.Menu(root)
    
    root.config(menu=menubar)
    
    
    file_menu = tk.Menu(menubar, tearoff=0)
    
    menubar.add_cascade(label="File", menu=file_menu)
    
    file_menu.add_command(label="New", command=new_file)
    
    file_menu.add_command(label="Open", command=open_file)
    
    file_menu.add_command(label="Save", command=save_file)
    
    file_menu.add_separator()
    
    file_menu.add_command(label="Exit", command=root.quit)
    
    
    # Create text area with scrollbar
    text_frame = tk.Frame(root)
    
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    
    text_area = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 11))
    
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    
    scrollbar = tk.Scrollbar(text_frame)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    text_area.config(yscrollcommand=scrollbar.set)
    
    scrollbar.config(command=text_area.yview)
    
    
    root.mainloop()


# Uncomment to run: create_text_editor()

EXAMPLE 5: STUDENT GRADE CALCULATOR
===================================

from tkinter import messagebox


def create_grade_calculator():
    
    root = tk.Tk()
    
    root.title("Student Grade Calculator")
    
    root.geometry("450x400")
    
    
    # Variables
    grades = []
    
    
    def add_grade():
        
        try:
            
            grade = float(grade_entry.get())
            
            if 0 <= grade <= 100:
                
                grades.append(grade)
                
                update_display()
                
                grade_entry.delete(0, tk.END)
                
            else:
                
                messagebox.showerror("Error", "Grade must be between 0 and 100")
                
        except ValueError:
            
            messagebox.showerror("Error", "Please enter a valid number")
    
    
    def remove_grade():
        
        try:
            
            selected_index = grade_listbox.curselection()[0]
            
            del grades[selected_index]
            
            update_display()
            
        except IndexError:
            
            messagebox.showwarning("Warning", "Please select a grade to remove")
    
    
    def calculate_stats():
        
        if not grades:
            
            messagebox.showwarning("Warning", "No grades entered")
            
            return
        
        
        average = sum(grades) / len(grades)
        
        highest = max(grades)
        
        lowest = min(grades)
        
        
        # Determine letter grade
        if average >= 90:
            
            letter_grade = "A"
            
        elif average >= 80:
            
            letter_grade = "B"
            
        elif average >= 70:
            
            letter_grade = "C"
            
        elif average >= 60:
            
            letter_grade = "D"
            
        else:
            
            letter_grade = "F"
        
        
        # Update result labels
        avg_var.set(f"Average: {average:.2f}")
        
        highest_var.set(f"Highest: {highest}")
        
        lowest_var.set(f"Lowest: {lowest}")
        
        letter_var.set(f"Letter Grade: {letter_grade}")
    
    
    def update_display():
        
        grade_listbox.delete(0, tk.END)
        
        for i, grade in enumerate(grades):
            
            grade_listbox.insert(tk.END, f"{i+1}. {grade}")
        
        
        calculate_stats()
    
    
    # Create GUI elements
    tk.Label(root, text="Student Grade Calculator", 
             font=("Arial", 16, "bold")).pack(pady=10)
    
    
    # Grade entry frame
    entry_frame = tk.Frame(root)
    
    entry_frame.pack(pady=10)
    
    
    tk.Label(entry_frame, text="Enter Grade (0-100):", 
             font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    
    grade_entry = tk.Entry(entry_frame, font=("Arial", 10), width=10)
    
    grade_entry.pack(side=tk.LEFT, padx=5)
    
    
    tk.Button(entry_frame, text="Add Grade", command=add_grade, 
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    
    # Grade list frame
    list_frame = tk.Frame(root)
    
    list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    
    tk.Label(list_frame, text="Grades:", font=("Arial", 12, "bold")).pack()
    
    
    grade_listbox = tk.Listbox(list_frame, font=("Arial", 10), height=8)
    
    grade_listbox.pack(fill=tk.BOTH, expand=True, padx=20)
    
    
    tk.Button(list_frame, text="Remove Selected Grade", 
              command=remove_grade, font=("Arial", 10)).pack(pady=5)
    
    
    # Statistics frame
    stats_frame = tk.Frame(root)
    
    stats_frame.pack(pady=10)
    
    
    # Result variables
    avg_var = tk.StringVar(value="Average: --")
    
    highest_var = tk.StringVar(value="Highest: --")
    
    lowest_var = tk.StringVar(value="Lowest: --")
    
    letter_var = tk.StringVar(value="Letter Grade: --")
    
    
    tk.Label(stats_frame, textvariable=avg_var, font=("Arial", 10)).pack()
    
    tk.Label(stats_frame, textvariable=highest_var, font=("Arial", 10)).pack()
    
    tk.Label(stats_frame, textvariable=lowest_var, font=("Arial", 10)).pack()
    
    tk.Label(stats_frame, textvariable=letter_var, font=("Arial", 10, "bold")).pack()
    
    
    # Bind Enter key to add grade
    grade_entry.bind("<Return>", lambda event: add_grade())
    
    
    root.mainloop()


# Uncomment to run: create_grade_calculator()


EXAMPLE 6: DIGITAL CLOCK APPLICATION
====================================

from datetime import datetime


def create_digital_clock():
    
    root = tk.Tk()
    
    root.title("Digital Clock")
    
    root.geometry("400x200")
    
    root.configure(bg="black")
    
    
    # Clock variables
    time_var = tk.StringVar()
    
    date_var = tk.StringVar()
    
    
    def update_time():
        
        # Get current time and date
        now = datetime.now()
        
        current_time = now.strftime("%H:%M:%S")
        
        current_date = now.strftime("%A, %B %d, %Y")
        
        
        # Update the display
        time_var.set(current_time)
        
        date_var.set(current_date)
        
        
        # Schedule the next update after 1000ms (1 second)
        root.after(1000, update_time)
    
    
    # Create clock display
    time_label = tk.Label(root, textvariable=time_var, 
                         font=("Digital-7", 48, "bold"), 
                         fg="lime", bg="black")
    
    time_label.pack(expand=True)
    
    
    date_label = tk.Label(root, textvariable=date_var, 
                         font=("Arial", 16), 
                         fg="white", bg="black")
    
    date_label.pack()
    
    
    # Start the clock
    update_time()
    
    
    root.mainloop()


# Uncomment to run: create_digital_clock()

=====================================
7. PRACTICE EXERCISES
=====================================

EXERCISE 1: BASIC BUTTON COUNTER
================================

Create a GUI application with:
- A label showing a number (starting at 0)
- An "Increment" button that increases the number by 1
- A "Decrement" button that decreases the number by 1
- A "Reset" button that sets the number back to 0

SOLUTION 1:

def exercise_1_solution():
    
    root = tk.Tk()
    
    root.title("Button Counter")
    
    root.geometry("250x150")
    
    
    # Counter variable
    counter = tk.IntVar(value=0)
    
    
    def increment():
        
        counter.set(counter.get() + 1)
    
    
    def decrement():
        
        counter.set(counter.get() - 1)
    
    
    def reset():
        
        counter.set(0)
    
    
    # Create GUI elements
    tk.Label(root, text="Counter:", font=("Arial", 12)).pack(pady=10)
    
    
    counter_label = tk.Label(root, textvariable=counter, 
                            font=("Arial", 16, "bold"), fg="blue")
    
    counter_label.pack(pady=5)
    
    
    button_frame = tk.Frame(root)
    
    button_frame.pack(pady=10)
    
    
    tk.Button(button_frame, text="Increment", command=increment, 
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    tk.Button(button_frame, text="Decrement", command=decrement, 
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    tk.Button(button_frame, text="Reset", command=reset, 
              font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    
    root.mainloop()


# Uncomment to run: exercise_1_solution()

EXERCISE 2: TEMPERATURE CONVERTER
=================================

Create a temperature converter that:
- Has input fields for Celsius and Fahrenheit
- Has buttons to convert from Celsius to Fahrenheit and vice versa
- Shows the converted temperature in the appropriate field
- Handles invalid input gracefully

Formulas:
- Fahrenheit = (Celsius × 9/5) + 32
- Celsius = (Fahrenheit - 32) × 5/9

SOLUTION 2:


def exercise_2_solution():
    
    root = tk.Tk()
    
    root.title("Temperature Converter")
    
    root.geometry("350x200")
    
    
    # Variables
    celsius_var = tk.StringVar()
    
    fahrenheit_var = tk.StringVar()
    
    
    def celsius_to_fahrenheit():
        
        try:
            
            celsius = float(celsius_var.get())
            
            fahrenheit = (celsius * 9/5) + 32
            
            fahrenheit_var.set(f"{fahrenheit:.2f}")
            
        except ValueError:
            
            messagebox.showerror("Error", "Please enter a valid number for Celsius")
    
    
    def fahrenheit_to_celsius():
        
        try:
            
            fahrenheit = float(fahrenheit_var.get())
            
            celsius = (fahrenheit - 32) * 5/9
            
            celsius_var.set(f"{celsius:.2f}")
            
        except ValueError:
            
            messagebox.showerror("Error", "Please enter a valid number for Fahrenheit")
    
    
    # Create GUI elements
    tk.Label(root, text="Temperature Converter", 
             font=("Arial", 14, "bold")).pack(pady=10)
    
    
    # Celsius section
    celsius_frame = tk.Frame(root)
    
    celsius_frame.pack(pady=5)
    
    
    tk.Label(celsius_frame, text="Celsius:", font=("Arial", 10)).pack(side=tk.LEFT)
    
    celsius_entry = tk.Entry(celsius_frame, textvariable=celsius_var, 
                            font=("Arial", 10), width=10)
    
    celsius_entry.pack(side=tk.LEFT, padx=5)
    
    tk.Button(celsius_frame, text="Convert to °F", 
              command=celsius_to_fahrenheit, font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
    
    
    # Fahrenheit section
    fahrenheit_frame = tk.Frame(root)
    
    fahrenheit_frame.pack(pady=5)
    
    
    tk.Label(fahrenheit_frame, text="Fahrenheit:", font=("Arial", 10)).pack(side=tk.LEFT)
    
    fahrenheit_entry = tk.Entry(fahrenheit_frame, textvariable=fahrenheit_var, 
                               font=("Arial", 10), width=10)
    
    fahrenheit_entry.pack(side=tk.LEFT, padx=5)
    
    tk.Button(fahrenheit_frame, text="Convert to °C", 
              command=fahrenheit_to_celsius, font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
    
    
    root.mainloop()


# Uncomment to run: exercise_2_solution()

EXERCISE 3: COLOR PICKER APPLICATION
====================================
Create a color picker application that:
- Has three sliders for Red, Green, and Blue values (0-255)
- Shows the current RGB values as text
- Displays a color preview square that updates in real-time
- Has a button to show the hex color code

SOLUTION 3:

def exercise_3_solution():
    
    root = tk.Tk()
    
    root.title("Color Picker")
    
    root.geometry("400x350")
    
    
    # Variables
    red_var = tk.IntVar(value=128)
    
    green_var = tk.IntVar(value=128)
    
    blue_var = tk.IntVar(value=128)
    
    
    def update_color(*args):
        
        # Get RGB values
        r = red_var.get()
        
        g = green_var.get()
        
        b = blue_var.get()
        
        
        # Convert to hex
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        
        # Update color preview
        color_frame.configure(bg=hex_color)
        
        
        # Update RGB display
        rgb_label.configure(text=f"RGB: ({r}, {g}, {b})")
        
        
        # Update hex display
        hex_label.configure(text=f"HEX: {hex_color.upper()}")
    
    
    # Create GUI elements
    tk.Label(root, text="Color Picker", font=("Arial", 16, "bold")).pack(pady=10)
    
    
    # Red slider
    red_frame = tk.Frame(root)
    
    red_frame.pack(pady=5, padx=20, fill=tk.X)
    
    tk.Label(red_frame, text="Red:", font=("Arial", 10), width=6).pack(side=tk.LEFT)
    
    red_scale = tk.Scale(red_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                        variable=red_var, command=update_color)
    
    red_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    tk.Label(red_frame, textvariable=red_var, font=("Arial", 10), width=3).pack(side=tk.RIGHT)
    
    
    # Green slider
    green_frame = tk.Frame(root)
    
    green_frame.pack(pady=5, padx=20, fill=tk.X)
    
    tk.Label(green_frame, text="Green:", font=("Arial", 10), width=6).pack(side=tk.LEFT)
    
    green_scale = tk.Scale(green_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                          variable=green_var, command=update_color)
    
    green_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    tk.Label(green_frame, textvariable=green_var, font=("Arial", 10), width=3).pack(side=tk.RIGHT)
    
    
    # Blue slider
    blue_frame = tk.Frame(root)
    
    blue_frame.pack(pady=5, padx=20, fill=tk.X)
    
    tk.Label(blue_frame, text="Blue:", font=("Arial", 10), width=6).pack(side=tk.LEFT)
    
    blue_scale = tk.Scale(blue_frame, from_=0, to=255, orient=tk.HORIZONTAL, 
                         variable=blue_var, command=update_color)
    
    blue_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    tk.Label(blue_frame, textvariable=blue_var, font=("Arial", 10), width=3).pack(side=tk.RIGHT)
    
    
    # Color preview
    color_frame = tk.Frame(root, width=200, height=100, relief=tk.SUNKEN, bd=2)
    
    color_frame.pack(pady=20)
    
    color_frame.pack_propagate(False)
    
    
    # RGB and HEX labels
    rgb_label = tk.Label(root, text="RGB: (128, 128, 