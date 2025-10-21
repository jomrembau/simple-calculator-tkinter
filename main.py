from tkinter import *
import tkinter as tk

calculation_log = ""

def button_clicked(button_char):
    global calculation_log
    calculation_log = calculation_log + str(button_char)
    calculation_label.config(text=calculation_log)

def equals_clicked():
    global calculation_log
    try:
        result = eval(calculation_log)
        main_label.config(text=str(result))
    except:
        main_label.config(text="Error")
    calculation_log = ""

def clear_labels():
    main_label.config(text="0")
    calculation_label.config(text="")

win = tk.Tk()
win.title("Simple Calculator")
win.geometry('350x600')
win.config(bg="black")

for i in range(7):
    win.rowconfigure(i, weight=1)
for j in range(4):
    win.columnconfigure(j, weight=1)

calculation_label = Label(font=("Arial", 13), bg="black", fg="white", justify="right", anchor="e")
calculation_label.grid(row=0, column=0,columnspan=4, pady=15, padx=50, sticky="nsew")

main_label = Label(text="0", font=("Arial", 45), bg="black", fg="white", justify="right", anchor="e")
main_label.grid(row=1, column=0,columnspan=4, pady=15, padx=50, sticky="nsew")

clear_button = Button(text="clr", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=clear_labels)
clear_button.grid(row=2, column=0,columnspan=3, padx=10, pady=10, sticky="nsew")

division_button = Button(text="/", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked("/"))
division_button.grid(row=2, column=3, columnspan=2, padx=10, pady=10, sticky="nsew")

seven_button = Button(text="7", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(7))
seven_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

eight_button = Button(text="8", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(8))
eight_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

nine_button = Button(text="9", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(9))
nine_button.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

multiplication_button = Button(text="*", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked("*"))
multiplication_button.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

four_button = Button(text="4", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(4))
four_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

five_button = Button(text="5", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(5))
five_button.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

six_button = Button(text="6", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(6))
six_button.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

addition_button = Button(text="+", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked("+"))
addition_button.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

one_button = Button(text="1", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(1))
one_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

two_button = Button(text="2", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(2))
two_button.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

three_button = Button(text="3", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(3))
three_button.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

subtract_button = Button(text="-", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked("-"))
subtract_button.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

zero_button = Button(text="0", font=("Arial", 17), bg="silver", fg="white", justify="center", padx=15, command=lambda: button_clicked(0))
zero_button.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

equals_button = Button(text="=", font=("Arial", 17), bg="orange", fg="white", justify="center", padx=15, command=equals_clicked)
equals_button.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")

win.mainloop()  

