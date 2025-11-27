import tkinter as tk
from tkinter import messagebox

def multiply_numbers():
    try:
        num1 = float(entry_num1.get())  
        num2 = float(entry_num2.get()
        result = num1 * num2
        result_label.config(text=f"Result: {result}") 
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.") 

root = tk.Tk()
root.title("Multiplication App")
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
