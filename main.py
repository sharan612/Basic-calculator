from tkinter import *
import customtkinter as ctk


# ♡ Calculator ♡

calc = ctk.CTk()
calc.geometry("650x650")
calc.config(bg="#F1F9FA")
calc.title("Calculator")
calc.resizable(False, False)

# ------------------ FUNCTIONS ------------------

Label=ctk.CTkLabel(calc, text= "sharan", text_color="#4E729C", bg_color="#F1F9FA", font=("Times", 10)).pack(side="bottom", anchor="se", padx=(0,5), pady=(0, 3))

expression=""

def press(value):
    global expression

    expression += str(value)

    display.delete(0, "end")
    display.insert(0, expression)

def clear_display():
    global expression

    expression = ""

    display.delete(0, "end")

def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, "end")
    display.insert(0, expression)

def calculate():
    global expression

    try:
        result = str(eval(expression))

        display.delete(0, "end")
        display.insert(0, result)

        expression = result

    except:
        display.delete(0, "end")
        display.insert(0, "Error")

        expression = ""

def key_press(event):
    key = event.keysym

    if key in ["0","1","2","3","4","5","6","7","8","9"]:
        press(key)

    elif key in ["plus", "KP_Add"]:
        press("+")

    elif key in ["minus", "KP_Subtract"]:
        press("-")

    elif key in ["asterisk", "KP_Multiply"]:
        press("*")

    elif key in ["slash", "KP_Divide"]:
        press("/")

    elif key == "period":
        press(".")

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear_display()

# ------------------ MAIN WINDOW ------------------

calc_frame=ctk.CTkFrame(calc, width=500, height=580, corner_radius=15, fg_color="#F7DAE1", bg_color="#F1F9FA")
calc_frame.place(relx=0.5, rely=0.5, anchor="center")

# ------------------ DISPLAY ------------------

display = ctk.CTkEntry(calc_frame, width=400, height=90, corner_radius=15, justify="right", font=("Arial", 30), border_color="#FA8DA8", border_width=2
                       , placeholder_text="0")
display.grid(row=0, column=0, columnspan=4, padx=20, pady=(20,15), sticky="ew")

# ------------------ BUTTONS ------------------

operators = ["+","-","*","/","=","C","♡"]

buttons = [
    ("C",1,0),
    ("⌫",1,1),
    ("%",1,2),
    ("/",1,3),

    ("7",2,0,),
    ("8",2,1),
    ("9",2,2),
    ("*",2,3),

    ("4",3,0),
    ("5",3,1),
    ("6",3,2),
    ("-",3,3),

    ("1",4,0),
    ("2",4,1),
    ("3",4,2),
    ("+",4,3),

    ("♡",5,0),
    ("0",5,1),
    (".",5,2),
    ("=",5,3)
]

for text, row, col in buttons:

    if text in operators:
        color = "#FCB2C4"
    else:
        color = "#F8DEE4"

    if text == "C":
        command = clear_display 
    elif text == "⌫":
        command = backspace
    elif text == "=":
        command = calculate
    else:
        command = lambda t=text: press(t)

    btns = ctk.CTkButton(calc_frame, text=text, fg_color=color, width=80, height=80, corner_radius=40, text_color="#000000", hover_color="#F891AB"
                         , border_color="#FA8DA8", border_width=2, command=command)

    if col == 0:
        xpad = (15, 3)
    elif col == 3:
        xpad = (3, 15)
    else:
        xpad = 3

    if row == 5:
        ypad = (3, 15)
    else:
        ypad = 3

    btns.grid(row=row, column=col, padx=xpad, pady=ypad)

calc.bind("<Key>", key_press)

calc.mainloop()