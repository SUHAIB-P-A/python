from tkinter import *
import tkinter.font as font
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()  # object

window.geometry("400x600")
window.config(bg="#e0ffff")
window.title("calculator")
# icon= tk.PhotoImage(r"C:/Users/Suhaib/learnPy/calculator/calculator_jP3_icon.ico")
# image load using PIL
icon = Image.open(
    "C:\\Users\\Suhaib\\learnPy\\calculator\\calculator_jP3_icon.ico")
icon = ImageTk.PhotoImage(icon)
# call the image
window.tk.call('wm', 'iconphoto', window._w, '-default', icon)
# window.iconbitmap('calculator\calculator_jP3_icon.ico')

# manage the button click


def Button_click(text):
    if (text == "C"):
        clear_screen()
    elif (text == "="):
        result()
    else:
        append_screen(text)

# clear the entry field


def clear_screen():
    calculator_screen.delete(0, tk.END)

# result display func


def result():
    try:
        result = str(eval(calculator_screen.get()))
        calculator_screen.delete(0, tk.END)
        calculator_screen.insert(0, result)
    except EXCEPTION:
        calculator_screen.delete(0, tk.END)
        calculator_screen.insert(0, "error")

# add one or more values on the entry field


def append_screen(text):
    current_text = calculator_screen.get()
    calculator_screen.delete(0, tk.END)
    calculator_screen.insert(0, current_text+text)
    print(current_text)


# TextBox
calculator_screen = tk.Entry(window, font=(
    "Helvetica", 20), bg="#d1d4dc", justify=RIGHT)
calculator_screen.grid(row=0, column=0, columnspan=4,
                       padx=10, pady=10, ipadx=31.25, ipady=31.25)


f = font.Font(size=20)
# buttons
button1 = Button(window, text="1", font=f, bg='#00e4f5',
                 command=lambda: Button_click("1"))
button2 = Button(window, text="2", font=f, bg='#00e4f5',
                 command=lambda: Button_click("2"))
button3 = Button(window, text="3", font=f, bg='#00e4f5',
                 command=lambda: Button_click("3"))
button4 = Button(window, text="4", font=f, bg='#00e4f5',
                 command=lambda: Button_click("4"))
button5 = Button(window, text="5", font=f, bg='#00e4f5',
                 command=lambda: Button_click("5"))
button6 = Button(window, text="6", font=f, bg='#00e4f5',
                 command=lambda: Button_click("6"))
button7 = Button(window, text="7", font=f, bg='#00e4f5',
                 command=lambda: Button_click("7"))
button8 = Button(window, text="8", font=f, bg='#00e4f5',
                 command=lambda: Button_click("8"))
button9 = Button(window, text="9", font=f, bg='#00e4f5',
                 command=lambda: Button_click("9"))
button0 = Button(window, text="0", font=f, bg='#00e4f5',
                 command=lambda: Button_click("0"))
buttonok = Button(window, text="=", font=f, bg='#00e4f5',
                  command=lambda: Button_click("="))
buttondot = Button(window, text="C", font=f, bg='#00e4f5',
                   command=lambda: Button_click("C"))
buttonplus = Button(window, text="+", font=f, bg='#00e4f5',
                    command=lambda: Button_click("+"))
buttonsub = Button(window, text="-", font=f, bg='#00e4f5',
                   command=lambda: Button_click("-"))
buttondiv = Button(window, text="/", font=f, bg='#00e4f5',
                   command=lambda: Button_click("/"))
buttonmul = Button(window, text="*", font=f, bg='#00e4f5',
                   command=lambda: Button_click("*"))

# arrange the button(matrix or grid)
button7.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=20)
button8.grid(row=1, column=1, padx=10, pady=10, ipadx=20, ipady=20)
button9.grid(row=1, column=2, padx=10, pady=10, ipadx=20, ipady=20)
button4.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=20)
button5.grid(row=2, column=1, padx=10, pady=10, ipadx=20, ipady=20)
button6.grid(row=2, column=2, padx=10, pady=10, ipadx=20, ipady=20)
button1.grid(row=3, column=0, padx=10, pady=10, ipadx=20, ipady=20)
button2.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20)
button3.grid(row=3, column=2, padx=10, pady=10, ipadx=20, ipady=20)
button0.grid(row=4, column=0, padx=10, pady=10, ipadx=20, ipady=20)
buttonok.grid(row=4, column=1, padx=10, pady=10, ipadx=20, ipady=20)
buttondot.grid(row=4, column=2, padx=10, pady=10, ipadx=20, ipady=20)
buttonplus.grid(row=1, column=3, padx=10, pady=10, ipadx=20, ipady=20)
buttondiv.grid(row=2, column=3, padx=10, pady=10, ipadx=20, ipady=20)
buttonmul.grid(row=3, column=3, padx=10, pady=10, ipadx=20, ipady=20)
buttonsub.grid(row=4, column=3, padx=10, pady=10, ipadx=20, ipady=20)


window.mainloop()
