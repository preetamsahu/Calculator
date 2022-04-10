from tkinter import *
import  tkinter.colorchooser as tcc
window=Tk()
window.wm_iconbitmap("calc.ico")
def clck(event):
    global expression_var
    text=event.widget.cget("text")
    if text=='=':
        if expression_var.get().isdigit():
            value=int(expression_var.get())

        else:
            try:
                value=eval(expression.get())

            except Exception as e:
                print(e)
                value="Error"

            expression_var.set(value)
            expression.update()
    elif text=="C":
        expression_var.set("")
        expression.update()

    else:
        expression_var.set(expression_var.get()+text)
        expression.update()
def clear(evenr):
    expression_var.set("")

def calculate(event):
    global expression_var
    if expression_var.get().isdigit():
        value = int(expression_var.get())

    else:
        try:
            value = eval(expression.get())

        except Exception as e:
            print(e)
            value = "Error"

        expression_var.set(value)
        expression.update()

def backspace(event):
    pass

def color(event):
    global clr
    clr=tcc.askcolor()
    window.config(background=clr[1])
    frame1.config(background=f"{clr[1]}")
    frame2.config(background=f"{clr[1]}")
    frame3.config(background=f"{clr[1]}")
    frame4.config(background=f"{clr[1]}")
    frame5.config(background=f"{clr[1]}")
    frame6.config(background=f"{clr[1]}")


def names(event):
    pass
myname=Label(window,text="Calculator",borderwidth=12,relief=SUNKEN,font="monaco 34 underline",fg="black")
myname.pack()

window.geometry("700x600")
window.title("My Calculator")
window.configure(background="light green")
#window.wm_iconbitmap("calc2.ico")
frame=Frame(window)
frame.pack()


expression_var=StringVar()
expression=Entry(window,width=30,font="Comicsansms 23 bold",textvariable=expression_var)
expression.pack(pady=12)

frame1=Frame(window)
frame1.config(background="light green")
frame1.pack(padx=12,pady=5)

#1 to 5 and Backspace
frame2 = Frame(window)
frame2.config(background="light green")
frame2.pack(pady=5)

btn1=Button(frame2,text="1",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame2,text="2",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame2,text="3",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame2,text="4",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame2,text="5",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn4=Button(frame2,text="<--BackSpace",font="comicsansms 20 italic",padx=12)
btn4.pack(side=RIGHT,padx=12,pady=12)
btn4.bind("<Button-1>",backspace)

#6 to 0 and clearscreen
frame3 = Frame(window)
frame3.config(background="light green")
frame3.pack(pady=5)

btn1=Button(frame3,text="6",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame3,text="7",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame3,text="8",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame3,text="9",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame3,text="0",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn2=Button(frame3,text="Clear Screen",font="Comicsansms 20 bold")
btn2.pack(side=LEFT,padx=12,pady=12)
btn2.bind("<Button-1>",clear)

#Airthmatic operation and calculate
frame4 = Frame(window,bg="light green")
frame4.pack(pady=5)

btn1=Button(frame4,text="=",font="comicsansms 20 italic",bg="grey",padx=12)
btn1.pack(side=LEFT,padx=12,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame4,text="/",font="comicsansms 20 italic",bg="grey",padx=15)
btn1.pack(side=LEFT,padx=15,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame4,text="*",font="comicsansms 20 italic",bg="grey",padx=15)
btn1.pack(side=LEFT,padx=15,pady=12)
btn1.bind("<Button-1>",clck)

btn1=Button(frame4,text="-",font="comicsansms 20 italic",bg="grey",padx=15)
btn1.pack(side=LEFT,padx=15,pady=5)
btn1.bind("<Button-1>",clck)

btn1=Button(frame4,text="+",font="comicsansms 20 italic",bg="grey",padx=10)
btn1.pack(side=LEFT,padx=15,pady=5)
btn1.bind("<Button-1>",clck)

btn3=Button(frame4,text="Calculate",font="Comicsansms 20 bold")
btn3.pack(side=LEFT,padx=15,pady=12)
btn3.bind("<Button-1>",calculate)


#next frame buttons backspace and theme
frame6=Frame(window)
frame6.config(background="light green")
frame6.pack()

btn4=Button(frame6,text="Theame",font="comicsansms 20 italic",padx=12)
btn4.pack(side=RIGHT,padx=12,pady=12)
btn4.bind("<Button-1>",color)

btn4=Button(frame6,text="Change Name",font="comicsansms 20 italic",padx=12)
btn4.pack(side=RIGHT,padx=12,pady=12)
btn4.bind("<Button-1>",names)


window.mainloop()
