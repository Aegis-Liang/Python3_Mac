from tkinter import *

root = Tk()

e = Entry(root, width=20)
e.insert(0, "Input Something Here...")
e.pack()

def myClick():
    myLabel = Label(root, text="Hi " + e.get())
    myLabel.pack()


myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="#FF0000")
myButton.pack()

root.mainloop()
