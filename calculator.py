from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set('error')
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Calculator")
    gui.geometry("400x400")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=5, ipadx=80)

    # Numbers
    Button(gui, text=1, command=lambda: press(1), width=10).grid(row=2, column=0)
    Button(gui, text=2, command=lambda: press(2), width=10).grid(row=2, column=1)
    Button(gui, text=3, command=lambda: press(3), width=10).grid(row=2, column=2)

    Button(gui, text=4, command=lambda: press(4), width=10).grid(row=3, column=0)
    Button(gui, text=5, command=lambda: press(5), width=10).grid(row=3, column=1)
    Button(gui, text=6, command=lambda: press(6), width=10).grid(row=3, column=2)

    Button(gui, text=7, command=lambda: press(7), width=10).grid(row=4, column=0)
    Button(gui, text=8, command=lambda: press(8), width=10).grid(row=4, column=1)
    Button(gui, text=9, command=lambda: press(9), width=10).grid(row=4, column=2)

    Button(gui, text=0, command=lambda: press(0), width=10).grid(row=5, column=0)

    # Operators
    Button(gui, text='+', command=lambda: press("+"), width=10).grid(row=2, column=3)
    Button(gui, text='-', command=lambda: press("-"), width=10).grid(row=3, column=3)
    Button(gui, text='*', command=lambda: press("*"), width=10).grid(row=4, column=3)
    Button(gui, text='/', command=lambda: press("/"), width=10).grid(row=5, column=3)

    # Equal and Clear
    Button(gui, text='=', command=equalpress, width=10).grid(row=5, column=2)
    Button(gui, text='C', command=clear, width=10).grid(row=5, column=1)

    # Decimal
    Button(gui, text='.', command=lambda: press("."), width=10).grid(row=6, column=0)

    gui.mainloop()