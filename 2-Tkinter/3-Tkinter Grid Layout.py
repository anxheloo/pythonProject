from tkinter import*   #tkinter is used to create applications with GUI

#Window(Is a container) - Frame(Another Container inside Window) - Widgets

#1-We need to create a window
root = Tk()

#Creating 2 Labels : root means that it belongs to the root window, text for text display
label1 = Label(root, text="Firstname")
label2 = Label(root, text="Lastname")

#We need something to accept input from user: textfields which in 2-Tkinter is called entries
entry1 = Entry(root)
entry2 = Entry(root)

#We need to arrange this items into a grid format
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

#This put the window in a loop so it only closes when we hit the close button
root.mainloop()
