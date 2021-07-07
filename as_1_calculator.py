# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:44:59 2021

@author: ACER
"""

import tkinter as tk
from tkinter import *


expression = ""
 
def press(num):
    """ getting the number input"""
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
def equal():
    """ Eval the expression """
    
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
        
    except:
        equation.set(" error ")
        expression = ""
 
def clr():
    """ clear function """
    global expression
    expression = ""
    equation.set("")
    

def them():
    """ theme """
    fg_col="black"
    bg_col="white"
    
    disp.config(fg=fg_col, bg=bg_col)
    button1.config(bg=bg_col, fg=fg_col)
    button2.config(bg=bg_col, fg=fg_col)
    button3.config(bg=bg_col, fg=fg_col)
    button4.config(bg=bg_col, fg=fg_col)
    button5.config(bg=bg_col, fg=fg_col)
    button6.config(bg=bg_col, fg=fg_col)
    button7.config(bg=bg_col, fg=fg_col)
    button8.config(bg=bg_col, fg=fg_col)
    button9.config(bg=bg_col, fg=fg_col)
    button0.config(bg=bg_col, fg=fg_col)
    button11.config(bg=bg_col, fg=fg_col)
    button12.config(bg=bg_col, fg=fg_col)
    button13.config(bg=bg_col, fg=fg_col)
    button14.config(bg=bg_col, fg=fg_col)
    button15.config(bg=bg_col, fg=fg_col)
    button16.config(bg=bg_col, fg=fg_col)
    button17.config(bg=bg_col, fg=fg_col)

 
fg_col="white"
bg_col="black"

# init. gui
root = tk.Tk()

# setting geometry of window
root.geometry("400x500")

# setting min size
root.minsize(400, 500)

# setting max size
root.maxsize(400, 500)

# setting icon
root.wm_iconbitmap("cal.ico")

# setting title of window
root.title("Tkt Calculator")

# creating a menu bar
MenuBar = Menu(root)

# adding menu to it
FMenu = Menu(MenuBar, tearoff=0, fg=fg_col, bg=bg_col)
FMenu.add_command(label="clear", command=clr)
FMenu.add_command(label="light theme", command=them)
FMenu.add_command(label="Exit", command=root.destroy)

MenuBar.add_cascade(label="Menu", menu=FMenu)
root.config(menu=MenuBar)

# making a frame to hold heading
frame0 = Frame(root)
Label(frame0, text="Simple Calculator", font="lucida 20 bold" ).pack()
frame0.pack(fill=X, ipadx=8, pady=10, padx=40)

equation = StringVar()

# making a frame to hold display screen 
frame1 = Frame(root)
disp = Entry(frame1, font="lucida 15 bold", textvariable=equation) #height=4, width=50)
disp.pack(fill=X, ipadx=8, pady=10, padx=40)
disp.config(fg="white", bg="black")
frame1.pack(fill=X)

# a frame to add space
frame2 = Frame(root)
Label(frame2, text=" ", font="lucida 5 bold" ).pack()
frame2.pack()

# a frame to hold all buttons
frame3 = Frame(root)

# <-- row 1-->
button1 = Button(frame3, text=' 7 ', fg=fg_col, bg=bg_col, command=lambda: press("7"), height=2, width=10)
button1.grid(row=2, column=0)

button2 = Button(frame3, text=' 8 ', fg=fg_col, bg=bg_col, command=lambda: press("8"), height=2, width=10)
button2.grid(row=2, column=1)

button3 = Button(frame3, text=' 9 ', fg=fg_col, bg=bg_col, command=lambda: press("9"), height=2, width=10)
button3.grid(row=2, column=2)

button4 = Button(frame3, text=' + ', fg=fg_col, bg=bg_col, command=lambda: press("+"), height=2, width=10)
button4.grid(row=2, column=3)

# <-- row 2-->
button5 = Button(frame3, text=' 4 ', fg=fg_col, bg=bg_col, command=lambda: press("4"), height=2, width=10)
button5.grid(row=3, column=0)

button6 = Button(frame3, text=' 5 ', fg=fg_col, bg=bg_col, command=lambda: press("5"), height=2, width=10)
button6.grid(row=3, column=1)

button7 = Button(frame3, text=' 6 ', fg=fg_col, bg=bg_col, command=lambda: press("6"), height=2, width=10)
button7.grid(row=3, column=2)

button8 = Button(frame3, text=' - ', fg=fg_col, bg=bg_col, command=lambda: press("-"), height=2, width=10)
button8.grid(row=3, column=3)

# <-- row 3-->
button9 = Button(frame3, text=' 1 ', fg=fg_col, bg=bg_col, command=lambda: press("1"), height=2, width=10)
button9.grid(row=4, column=0)

button0 = Button(frame3, text=' 2 ', fg=fg_col, bg=bg_col, command=lambda: press("2"), height=2, width=10)
button0.grid(row=4, column=1)

button11 = Button(frame3, text=' 3 ', fg=fg_col, bg=bg_col, command=lambda: press("3"), height=2, width=10)
button11.grid(row=4, column=2)

button12 = Button(frame3, text=' x ', fg=fg_col, bg=bg_col, command=lambda: press("*"), height=2, width=10)
button12.grid(row=4, column=3)

# <-- row 4-->
button13 = Button(frame3, text=' . ', fg=fg_col, bg=bg_col, command=lambda: press("."), height=2, width=10)
button13.grid(row=5, column=0)

button14 = Button(frame3, text=' 0 ', fg=fg_col, bg=bg_col, command=lambda: press("0"), height=2, width=10)
button14.grid(row=5, column=1)

button15 = Button(frame3, text=' = ', fg=fg_col, bg=bg_col, command=equal, height=2, width=10)
button15.grid(row=5, column=2)

button16 = Button(frame3, text=' / ', fg=fg_col, bg=bg_col, command=lambda: press("/"), height=2, width=10)
button16.grid(row=5, column=3)

frame3.pack()

# a frame to hold clear button
frame4 = Frame(root)
button17 = Button(frame4, text=' clear ', fg=fg_col, bg=bg_col, command=lambda: clr(), width=44, height=3)
button17.grid(row=5, column=1)
frame4.pack(expand=True)

# creating the main loop
root.mainloop()
