from tkinter import *
import tkinter.font as font
import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()# object 

window.geometry("500x500")
window.config(bg="#0e493e")
window.title("calculator")
#icon= tk.PhotoImage(r"C:/Users/Suhaib/learnPy/calculator/calculator_jP3_icon.ico")
icon = Image.open("C:\\Users\\Suhaib\\learnPy\\calculator\\calculator_jP3_icon.ico")
icon = ImageTk.PhotoImage(icon)
window.tk.call('wm', 'iconphoto', window._w,'-default', icon)
#window.iconbitmap('calculator\calculator_jP3_icon.ico')

f = font.Font(size=20)
# buttons
button1=Button(window,text="1",font=f)
button2=Button(window,text="2",font=f)
button3=Button(window,text="3",font=f)
button4=Button(window,text="4",font=f)
button5=Button(window,text="5",font=f)
button6=Button(window,text="6",font=f)
button7=Button(window,text="7",font=f)
button8=Button(window,text="8",font=f)
button9=Button(window,text="9",font=f)
button0=Button(window,text="0",font=f)
buttonok=Button(window,text="=",font=f)
buttondot=Button(window,text=".",font=f)
buttonplus=Button(window,text="+",font=f)
buttonsub=Button(window,text="-",font=f)
buttondiv=Button(window,text="/",font=f)
buttonmul=Button(window,text="*",font=f)

# arrange the button(matrix or grid)
button1.grid(row="2",column="0",ipadx="31.25",ipady="31.25")
button2.grid(row="2",column="1",ipadx="31.25",ipady="31.25")
button3.grid(row="2",column="2",ipadx="31.25",ipady="31.25")
button4.grid(row="1",column="0",ipadx="31.25",ipady="31.25")
button5.grid(row="1",column="1",ipadx="31.25",ipady="31.25")
button6.grid(row="1",column="2",ipadx="31.25",ipady="31.25")
button7.grid(row="0",column="0",ipadx="31.25",ipady="31.25")
button8.grid(row="0",column="1",ipadx="31.25",ipady="31.25")
button9.grid(row="0",column="2",ipadx="31.25",ipady="31.25")
button0.grid(row="3",column="1",ipadx="31.25",ipady="31.25")
buttonok.grid(row="3",column="2",ipadx="31.25",ipady="31.25")
buttondot.grid(row="3",column="0",ipadx="31.25",ipady="31.25")
buttonplus.grid(row="0",column="3",ipadx="31.25",ipady="31.25")
buttondiv.grid(row="1",column="3",ipadx="31.25",ipady="31.25")
buttonmul.grid(row="2",column="3",ipadx="31.25",ipady="31.25")
buttonsub.grid(row="3",column="3",ipadx="31.25",ipady="31.25")


window.mainloop()