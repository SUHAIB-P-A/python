from tkinter import *
import tkinter.font as font
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()  # object

window.geometry("400x600")
window.config(bg="#0e493e")
window.title("calculator")
# icon= tk.PhotoImage(r"C:/Users/Suhaib/learnPy/calculator/calculator_jP3_icon.ico")
# image load using PIL
icon = Image.open(
    "C:\\Users\\Suhaib\\learnPy\\calculator\\calculator_jP3_icon.ico")
icon = ImageTk.PhotoImage(icon)
# call the image
window.tk.call('wm', 'iconphoto', window._w, '-default', icon)
# window.iconbitmap('calculator\calculator_jP3_icon.ico')

#TextBox
calculator_screen = tk.Entry(window, font=("Helvetica", 20),bg="#d1d4dc")
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=31.25, ipady=31.25)


f = font.Font(size=20)
# buttons
button1 = Button(window, text="1", font=f)
button2 = Button(window, text="2", font=f)
button3 = Button(window, text="3", font=f)
button4 = Button(window, text="4", font=f)
button5 = Button(window, text="5", font=f)
button6 = Button(window, text="6", font=f)
button7 = Button(window, text="7", font=f)
button8 = Button(window, text="8", font=f)
button9 = Button(window, text="9", font=f)
button0 = Button(window, text="0", font=f)
buttonok = Button(window, text="=", font=f)
buttondot = Button(window, text=".", font=f)
buttonplus = Button(window, text="+", font=f)
buttonsub = Button(window, text="-", font=f)
buttondiv = Button(window, text="/", font=f)
buttonmul = Button(window, text="*", font=f)

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
