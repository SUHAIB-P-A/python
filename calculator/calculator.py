from tkinter import *

window=Tk()# object 

window.geometry("500x500")
window.config(bg="#0e493e")


# buttons
button1=Button(window,text="1")
button2=Button(window,text="2")
button3=Button(window,text="3")
button4=Button(window,text="4")
button5=Button(window,text="5")
button6=Button(window,text="6")
button7=Button(window,text="7")
button8=Button(window,text="8")
button9=Button(window,text="9")
button0=Button(window,text="0")
buttonok=Button(window,text="=")
buttondot=Button(window,text=".")
buttonplus=Button(window,text="+")
buttonsub=Button(window,text="-")
buttondiv=Button(window,text="/")
buttonmul=Button(window,text="*")

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