from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is ...")

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=5)

# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=1)
# myLabel2 = Label(root, text="My name is ...").grid(row=1, column=5)

root.mainloop()
