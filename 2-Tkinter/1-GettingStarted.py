from tkinter import*   #tkinter is used to create applications with GUI

#Window(Is a container) - Frame(Another Container inside Window) - Widgets

#1-We need to create a window
root = Tk()

#2-We create a label with 2 parameters: root which says that this label belongs to the root window and a text
label1 = Label(root,text="Hello World")

#3-Now we need to add our label to the window
label1.pack()

#4-When we hit run, we dont see anything cuz pc automatically creates and close our window really fast.
# We need to add smthng to keep it waiting

root.mainloop()  #This put the window in a loop so it only closes when we hit the close button



