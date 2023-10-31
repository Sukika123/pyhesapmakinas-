import tkinter as tk
import math

memory = 0
memory_in_use = False

def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(number))

def clear():
    input_field.delete(0, tk.END)

def evaluate():
    try:
        expression = input_field.get()
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
    except Exception:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Hata")

def square_root():
    try:
        number = float(input_field.get())
        result = math.sqrt(number)
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
    except Exception:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Hata")

def power():
    try:
        expression = input_field.get()
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(0, result ** 2)
    except Exception:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Hata")

def memory_clear():
    global memory
    memory = 0
    memory_in_use = False

def memory_recall():
    input_field.insert(0, memory)

def memory_add():
    global memory
    memory += float(input_field.get())

def memory_subtract():
    global memory
    memory -= float(input_field.get())

window = tk.Tk()
window.title("Hesap Makinesi")
window.geometry("300x300")
window.configure(bg='lightblue')

input_field = tk.Entry(window, width=30) 
input_field.grid(row=0, column=0, columnspan=4)  

buttons = [
    "1", "2", "3", "*",
    "4", "5", "6", "/",
    "7", "8", "9", "-",
    "C", "0", "=", "+",
    "MR", "MC", "M-", "M+",
    "^", "√"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, command=evaluate).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(window, text=button, width=5, height=2, command=clear).grid(row=row_val, column=col_val)
    elif button == "sqrt":
        tk.Button(window, text=button, width=5, height=2, command=square_root).grid(row=row_val, column=col_val)
    elif button == "^":
        tk.Button(window, text=button, width=5, height=2, command=power).grid(row=row_val, column=col_val)
    elif button == "MC":
        tk.Button(window, text=button, width=5, height=2, command=memory_clear).grid(row=row_val, column=col_val)
    elif button == "MR":
        tk.Button(window, text=button, width=5, height=2, command=memory_recall).grid(row=row_val, column=col_val)
    elif button == "M+":
        tk.Button(window, text=button, width=5, height=2, command=memory_add).grid(row=row_val, column=col_val)
    elif button == "M-":
        tk.Button(window, text=button, width=5, height=2, command=memory_subtract).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
